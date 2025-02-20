<script>
    import { onMount } from "svelte";
    import Textarea from "./components/textarea.svelte";
    import { theme } from "../stores";
</script>

<div class="wrapper" class:light-wrapper={!$theme} class:dark-wrapper={$theme}>
    <div class="logo">
        <h1>
            S<span class="dark-blue" class:light-dark-blue={!$theme} class:dark-dark-blue={$theme}>p</span>otted LO
        </h1>
        <h1>
            8 <span class="dark-blue" class:light-dark-blue={!$theme} class:dark-dark-blue={$theme}>P</span>oznań
        </h1>
    </div>
    
    <div class="text-area">
        <Textarea/>
    </div>
</div>

<style>
    .wrapper {
        height: calc(100vh - 40px); /* Subtract header height (40px) */
        width: 100vw;
        display: flex;
        flex-direction: column;
        transition: all .2s ease-in-out;
        overflow: hidden; /* Prevent overflow */
    }

    .logo {
        margin-top: 10px; /* Adjust to place it higher */
        margin-bottom: 0px;
        align-items: flex-start; /* Align text to the left */
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* Align items to the top */
        padding-left: 10vw;
        padding-right: 10vw;
        text-align: center;
        margin-bottom:40px;
    }

    .logo > h1 {
        font-size: 6vw;
        margin: 0; /* Remove default margin for cleaner alignment */
        font-weight: 600;
    }

    /* Adjust the space between the two h1 elements */
    .logo h1 + h1 {
        margin-top: -60px; /* Bring the second h1 closer to the first one */
    }

    .text-area {
        flex: 1; /* Fill remaining space */
        display: flex;
        justify-content: center; /* Keep text area centered */
        align-items: center;
        width: 100%;
        height:100%;
        overflow: hidden; /* Prevent scrolling inside text area */
        margin-top: -10vw;
    }

    .light-wrapper {
        background: white;
        color: black;
    }

    .dark-wrapper {
        background: #040F16;
        color: white;
    }

    /* Media Queries for responsiveness */
    @media (max-width: 1024px) {
        .logo > h1 {
            font-size: 8vw; /* Adjust font size for tablets */
        }

        .logo h1 + h1 {
            margin-top: -4vw; /* Adjust spacing for smaller screens */
        }

        .text-area {
            margin-top: -5vw; /* Adjust text area margin for smaller screens */
        }
    }

    @media (max-width: 768px) {
        .logo > h1 {
            font-size: 10vw; /* Adjust font size for mobile screens */
        }

        .logo h1 + h1 {
            margin-top: -3vw; /* Adjust spacing between titles */
        }

        .text-area {
            margin-top: -4vw;
        }

        .wrapper {
            height: calc(100vh - 20px); /* Adjust for smaller header */
        }
    }

    @media (max-width: 480px) {
        .logo > h1 {
            font-size: 12vw; /* Even larger font for small mobile screens */
        }

        .logo h1 + h1 {
            margin-top: -2vw; /* Adjust spacing further */
        }

        .text-area {
            margin-top: -3vw;
        }

        .wrapper {
            height: 100vh; /* Take full height on mobile */
        }
    }

    /* Styling the 'p' letter inside the h1 */
    .dark-blue {
        text-shadow:0 13px 17px rgba(31, 4, 151, 0.3);
    }

    .dark-dark-blue{
        color: #58a4f0;
    }

    .light-dark-blue{
        color: #013e7a;
    }
</style>
