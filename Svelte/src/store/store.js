import { writable } from 'svelte/store';
import { createUserWithEmailAndPassword, signInWithEmailAndPassword } from 'firebase/auth';
import { auth } from '../lib/firebase/firebase';

export const authStore = writable({
    user: null,
    loading: true,
    data: null
});

export const authHandlers = {
    login: async (email, password) => {
        await signInWithEmailAndPassword(auth, email, password);
    },
    signup: async (email, password) => {
        await createUserWithEmailAndPassword(auth, email, password);
    }
};