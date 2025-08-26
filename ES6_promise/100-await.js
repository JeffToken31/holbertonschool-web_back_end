import { uploadPhoto, createUser } from './utils.js';

export default async function asyncUploadUser () {
  try {
    const photo = await uploadPhoto();
    const user = await createUser();
    const result = { photo, user };
    return result;
  } catch (error) {
    return {
      photo: null,
      user: null
    };
  }
}
