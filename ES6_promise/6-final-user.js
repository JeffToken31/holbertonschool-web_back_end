import signUpUser from "./4-user-promise.js";
import uploadPhoto from "./5-photo-reject.js";

export default function handleProfileSignup(firstName, lastName, filename) {
	return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(filename)])
		.then(([responses]) => {
			responses.map((resp) => {
				if(resp.status === 'fulfilled') {
				return {
					status: resp.status,
					value: resp.value,
					}
			} else {
				return {
					status: resp.status,
					value: resp.reason,
					}
				}
			})
	})
}