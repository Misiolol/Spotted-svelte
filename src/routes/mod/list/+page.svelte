<script>
    import { theme } from "../../../stores";
    //import { telle } from "../../../stores";
    
    let telle = ["bajka", "jajko"]
</script>

<div class="wrapper" class:light-wrapper={!$theme} class:dark-wrapper={$theme}>
    <main>
        {#each telle as tell, index}
        <div class="tell" class:light-tell={!$theme} class:dark-tell={$theme}>
            <p>{index + 1}. {tell}</p>
            <div class="telle-action-icons">
                <svg class = "check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" class:light-icon={!$theme} class:dark-icon={$theme}><path d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/></svg>
                <svg class = "edit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class:light-icon={!$theme} class:dark-icon={$theme}><path d="M410.3 231l11.3-11.3-33.9-33.9-62.1-62.1L291.7 89.8l-11.3 11.3-22.6 22.6L58.6 322.9c-10.4 10.4-18 23.3-22.2 37.4L1 480.7c-2.5 8.4-.2 17.5 6.1 23.7s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L387.7 253.7 410.3 231zM160 399.4l-9.1 22.7c-4 3.1-8.5 5.4-13.3 6.9L59.4 452l23-78.1c1.4-4.9 3.8-9.4 6.9-13.3l22.7-9.1 0 32c0 8.8 7.2 16 16 16l32 0zM362.7 18.7L348.3 33.2 325.7 55.8 314.3 67.1l33.9 33.9 62.1 62.1 33.9 33.9 11.3-11.3 22.6-22.6 14.5-14.5c25-25 25-65.5 0-90.5L453.3 18.7c-25-25-65.5-25-90.5 0zm-47.4 168l-144 144c-6.2 6.2-16.4 6.2-22.6 0s-6.2-16.4 0-22.6l144-144c6.2-6.2 16.4-6.2 22.6 0s6.2 16.4 0 22.6z"/></svg>
                <svg class = "deny" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class:light-icon={!$theme} class:dark-icon={$theme}><path d="M367.2 412.5L99.5 144.8C77.1 176.1 64 214.5 64 256c0 106 86 192 192 192c41.5 0 79.9-13.1 111.2-35.5zm45.3-45.3C434.9 335.9 448 297.5 448 256c0-106-86-192-192-192c-41.5 0-79.9 13.1-111.2 35.5L412.5 367.2zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256z"/></svg>
            </div>
        </div>
        {/each}
    </main>
</div>



<style>
    *{
        transition: all .2s ease-in-out;
    }

    .wrapper{
        height: calc(100vh - 40px); /* Subtract header height (40px) */
        width: 100vw;
        display: flex;
        flex-direction: column;
        overflow: hidden; /* Prevent overflow */
        background-color: red;
        align-items: center;

    }

    .light-wrapper {
        background: white;
    }

    .dark-wrapper {
        background: #040F16;
    }

    .light-tell {
        color: black;
    }

    .dark-tell {
        color: white;
    }

    .tell{

        padding:10px 14px;
        display:flex;
        align-items: center;
        justify-content: space-between;
        width:80vw;
    }

    .telle-action-icons {
        display: flex;
        align-items: center;
        justify-content: center; /* Center the icons */
        height: 5vw;
        width: auto; /* Allow dynamic width */
        gap: 20px; /* Space between icons */
        padding: 10px; /* Adds padding for better spacing */
    }

    .telle-action-icons > svg {
        width: 40px; /* Increase icon size */
        height: 40px; /* Increase icon size */
        padding: 5px; /* Adjust padding */
        cursor: pointer;
    }

    .telle-action-icons > svg:hover {
        transform:scale(1.2);
        cursor: pointer;
    }

    .check{
        fill:green !important;
        width: 60px; /* Increase icon size */
        height: 60px; /* Increase icon size */
    }

    .deny{
        fill:red !important;
    }


    .light-icon{
        fill:black;
    }

    .dark-icon{
        fill:white;
    }
</style>
