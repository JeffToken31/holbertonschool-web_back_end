import signUpUser from "./4-user-promise.js";
import uploadPhoto from "./5-photo-reject.js";

export default function handleProfileSignup(firstName, lastName, filename) {
	return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(filename)])
		.then((responses) => {
			return responses.map((response) => ({
				status: response.status,
				value: response.value || response.reason,
			}))
	})
}