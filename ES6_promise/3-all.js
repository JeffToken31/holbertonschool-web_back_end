import { uploadPhoto, createUser } from "./utils.js";

export default function handleProfileSignup() {
    Promise.all([uploadPhoto(), createUser()])
      .then(([rep1, rep2]) =>
        console.log(`${rep1.body} ${rep2.firstName} ${rep2.lastName}`)
      )
      .catch(() => console.log('Signup system offline'));
}