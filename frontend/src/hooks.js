import * as cookie from 'cookie';

async function getUserInformation(cookiee) {
    const cookies = cookie.parse(cookiee || '');
    if (cookies.jwt) {
        const opts = {
            headers: {
                cookie: cookiee
            }
        };
        const res = fetch(
            'http://backend:4000/user/me',
            opts
        ).then((r) => r.json());
        if (res.detail) {
            return null
        }
        return res
    } else {
        return null;
    }
}

/** @type {import('@sveltejs/kit').Handle} */
export async function handle({ request, resolve }) {
	request.locals.user = await getUserInformation(request.headers.cookie);

	const response = await resolve(request);

	return {
		...response,
		headers: {
			...response.headers
		}
	};
}

/** @type {import('@sveltejs/kit').GetSession} */
export function getSession(request) {
    // console.log(request.locals.user);
    return request.locals.user
        ? {
            user: request.locals.user
        }
        : {};
}


/** @type {import('@sveltejs/kit').ExternalFetch} */
export async function externalFetch(request) {
    if (request.url.startsWith('http://localhost:3000/backend/')) {
        // clone the original request, but change the URL to backend container
        request = new Request(
            request.url.replace('http://localhost:3000/backend/', 'http://backend:4000/'),
            request
        );
    }

    return fetch(request);
}