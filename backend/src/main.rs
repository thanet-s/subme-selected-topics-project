use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};

#[get("/")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[post("/echo")]
async fn echo(req_body: String) -> impl Responder {
    HttpResponse::Ok().body(req_body)
}

use actix_web::middleware::Logger;
use env_logger::Env;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    env_logger::Builder::from_env(Env::default().default_filter_or("info")).init();

    HttpServer::new(|| {
        App::new()
            .wrap(Logger::new("%t \"%r %s\" \"%{x-forwarded-for}i %{User-Agent}i\" %T"))
            .service(
                web::scope("/api")
                    .service(hello)
                    .service(echo)
            )
    })
    .bind("0.0.0.0:4000")?
    .run()
    .await
}