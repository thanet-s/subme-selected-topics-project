export function login(endpoint, data) {
	return fetch(endpoint, {
		method: 'POST',
		credentials: 'include',
		body: data
	}).then((r) => r.json());
}