FROM rust:1.55
WORKDIR /usr/src/subme-backend
RUN apt-get update && apt-get install lld -y && cargo install cargo-watch
EXPOSE 4000
CMD cargo watch -x run