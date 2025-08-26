import { uploadPhoto, createUser } from "./utils.js";

export default function handleProfileSignup() {
    const photos = uploadPhoto();
    const user = createUser();
    Promise.all([photos, user])
      .then(([rep1, rep2]) =>
        console.log(`${rep1.body} ${rep2.firstName} ${rep2.lastName}`)
      )
      .catch(() => new Error('Signup system offline'));
}