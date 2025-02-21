<script>
    import { theme } from "../stores";
    import { telle } from "../stores";
    let currentTell = ''
    let error = true;
    function addTell(){
        error = false;
        if(!currentTell){
            error = true;
        }
        telle.update(items => [...items, currentTell]);
        console.log({$telle})
        currentTell = "";
    }
</script>

<div class="message-box" class:light-message={!$theme} class:dark-message={$theme}>
    <form class="form-container">
        <textarea bind:value={currentTell} id="message" rows="4" placeholder="Text"></textarea>
        <button onclick={addTell} type="button" class="btn-send" class:light-btn={!$theme} class:dark-btn={$theme}>Wyślij</button>
    </form>
</div>

<style>
    .dark-btn, .light-btn {
        transition: all .2s ease-in-out;
        margin-top: 10px;
        width: 300px;
        height: 40px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 1rem;
        font-weight: 500;
        padding: 10px;
        display: flex;
        flex-direction: column;
        align-items: center; /* Aligns button to the right */
        justify-content: center;
    }

    /* Dark button styles */
    .dark-btn {
        background: white;
        color: black;
    }

    .dark-btn:hover {
        background: rgb(116, 114, 114);
        color: white;
    }

    /* Light button styles */
    .light-btn {
        background-color: black;
        color: white;
    }

    .light-btn:hover {
        background-color: rgb(116, 114, 114);
        color: white;
    }

    /* Hover state for both buttons */
    .dark-btn:hover, .light-btn:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* Darker shadow on hover */
    }

    .form-container {
        display: flex;
        flex-direction: column;
        align-items: flex-end; /* Aligns button to the right */
        width: 70vw; /* Increased width */
        max-width: 700px; /* Ensures it doesn't stretch too wide */
        margin: 0 auto;
    }

    .message-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        position: relative; /* Make sure the background extends outside the div */
        height:100%;
        width:100%;
    }

    #message {
        width: 100%;
        height: 15vw; /* Adjusted height */
        padding: 10px;
        font-size: 1rem;
        border-radius: 10px; /* Slightly larger rounded corners */
        border: 3px solid gray; /* Thicker border */
        resize: none;
        background-color: #f9f9f9;
        position: relative;
        z-index: 2; /* Make sure the text area is on top of the background */
        box-shadow: 0 13px 12px rgba(0, 0, 0, 0.2); /* Thicker drop shadow for more depth */
        transition: box-shadow 0.2s ease-in-out; /* Smooth transition for shadow */
    }

    #message:focus {
        border-color: #388ae7; /* Blue border on focus */
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.8); /* Stronger shadow on focus */
    }

    .dark-message {
        color: black;
        background: url('src/assets/poswiatad.png') no-repeat center center;
        background-size:50%;
        z-index: 1; /* Place the background behind the textarea */
    }

    .light-message {
        color: rgb(54, 54, 54);
        background: url('src/assets/poswiatab.png') no-repeat center center;
        background-size: 50%;
        z-index: 1; /* Place the background behind the textarea */
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .form-container {
            width: 90vw;
        }

        #message {
            height: 40vh;
        }

        .btn-send {
            width: 50%;
            font-size: 1.2rem;
            padding: 12px;
        }
    }
</style>
