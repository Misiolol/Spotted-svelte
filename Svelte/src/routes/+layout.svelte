<script>
    import '../app.css'
    import { theme } from "../stores"
    import {onMount} from 'svelte'
    import {auth, db} from "../lib/firebase/firebase"
    import { getDoc, doc, setDoc } from "firebase/firestore";
    import { authStore } from "../store/store";

    const nonAuthRoutes = ["/", "/mod"];

    onMount(() => {
        console.log("Mounting");
        const unsubscribe = auth.onAuthStateChanged(async (user) => {
            const currentPath = window.location.pathname;

            if (!user && !nonAuthRoutes.includes(currentPath)) {
                window.location.href = "/";
                return;
            }

            if (user && currentPath === "/mod") {
                window.location.href = "/mod/list";
                return;
            }

            if (!user) {
                return;
            }

            let dataToSetToStore;
            const docRef = doc(db, "users", user.uid);
            const docSnap = await getDoc(docRef);
            if (!docSnap.exists()) {
                console.log("Creating User");
                const userRef = doc(db, "users", user.uid);
                dataToSetToStore = {
                    email: user.email,
                    todos: [],
                };
                await setDoc(userRef, dataToSetToStore, { merge: true });
            } else {
                console.log("Fetching User");
                const userData = docSnap.data();
                dataToSetToStore = userData;
            }

            authStore.update((curr) => {
                return {
                    ...curr,
                    user,
                    data: dataToSetToStore,
                    loading: false,
                };
            });
        });
        return unsubscribe;
    });

    let { children } = $props();
    
    function toggleTheme(){
        theme.set(!$theme);
    }
</script>

<div class="header" class:light-header={!$theme} class:dark-header={$theme}>
    <div class="darkmode-toggle">
        <label class="inline-flex items-center cursor-pointer">
            <div class="toggle-wrapper" class:light-tgwrapper={!$theme} class:dark-tgwrapper={$theme}> 
                <input 
                    type="checkbox" 
                    value={theme}
                    class="sr-only peer" 
                    onclick={toggleTheme}
                />
                <img src="\src\assets\moon-dark-theme-svgrepo-com.svg" alt="img-dark-mode" class="toggle-icon">
                <div class="relative w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 dark:peer-focus:ring-blue-800 rounded-full peer dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-blue-600 dark:peer-checked:bg-blue-600"></div>
            </div>
        </label>
    </div>
</div>

{@render children()}


<style>
    .header {
        display: flex;
        align-items: center; /* Centers the toggle vertically */
        justify-content: flex-end; /* Align the toggler to the right */
        height: 60px; /* Make header taller */
        padding: 0 20px; /* Padding for spacing */
        transition: all .2s ease-in-out;
    }
    .dark-header{
        background:#040F16;
    }
    .light-header{
        background:white;
    }
    .darkmode-toggle {
        display: flex;
        align-items: center;
		justify-content: center;
    }

    .toggle-wrapper {
        transition: all .2s ease-in-out;
        display: flex;
        align-items: center; 
        border-radius: 8px;
        padding: 6px 12px; /* Increased padding for more space around the toggle */
    }
    .dark-tgwrapper {
        background: rgba(255, 255, 255, 0.4);
    }

    .light-tgwrapper {
        background: rgba(0, 0, 0, 0.4);
    }

    .toggle-icon {
        width: 20px; /* Dostosuj szerokość ikony */
        height: 20px; /* Dostosuj wysokość ikony */
        object-fit: contain; /* Zapewnia, że ikona zachowa swoje proporcje */
		margin-right:12px;
    }
</style>
