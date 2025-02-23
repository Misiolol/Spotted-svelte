<script>
    import { theme } from "../../../stores";
    //import { telle } from "../../../stores";
    
    let telle = ["bajka", "jajko"]
    let currentTell = ''
    let error = false;

    //*******************************//

    function addTell(){
        error = false;
        if(!currentTell){
            error = true;
        }
        telle = [...telle, currentTell];
        console.log({telle})
        currentTell = "";
    }

    function editTell(index){
        console.log(index);
        let newTelle = [...telle].filter((val, i) =>{
            console.log(i, index, i!==index)
            return i !== index;
        })
        currentTell = telle[index];
        telle = newTelle;
    }

    function removeTell(index){
        console.log(index);
        let newTelle = [...telle].filter((val, i) =>{
            console.log(i, index, i!==index)
            return i !== index;
        })
        telle = newTelle;
    }

</script>

<div class="wrapper" class:light-wrapper={!$theme} class:dark-wrapper={$theme}>
    <main>
        {#each telle as tell, index}
        <div class="tell" class:light-tell={!$theme} class:dark-tell={$theme}>
            <p>{index + 1}. {tell}</p>
            <div class="telle-action-icons">
            
                <!-- accept button -->
                <i><svg class = "check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class:light-icon={!$theme} class:dark-icon={$theme}><path d="M64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32zM337 209L209 337c-9.4 9.4-24.6 9.4-33.9 0l-64-64c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l47 47L303 175c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9z"/></svg></i>
                
                <!-- edit button -->
                <i role = "button" tabindex = {index} onclick={() => {
                    editTell(index);
                }} 
                onkeydown={() => {}}><svg class = "edit" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class:light-icon={!$theme} class:dark-icon={$theme}><path d="M410.3 231l11.3-11.3-33.9-33.9-62.1-62.1L291.7 89.8l-11.3 11.3-22.6 22.6L58.6 322.9c-10.4 10.4-18 23.3-22.2 37.4L1 480.7c-2.5 8.4-.2 17.5 6.1 23.7s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L387.7 253.7 410.3 231zM160 399.4l-9.1 22.7c-4 3.1-8.5 5.4-13.3 6.9L59.4 452l23-78.1c1.4-4.9 3.8-9.4 6.9-13.3l22.7-9.1 0 32c0 8.8 7.2 16 16 16l32 0zM362.7 18.7L348.3 33.2 325.7 55.8 314.3 67.1l33.9 33.9 62.1 62.1 33.9 33.9 11.3-11.3 22.6-22.6 14.5-14.5c25-25 25-65.5 0-90.5L453.3 18.7c-25-25-65.5-25-90.5 0zm-47.4 168l-144 144c-6.2 6.2-16.4 6.2-22.6 0s-6.2-16.4 0-22.6l144-144c6.2-6.2 16.4-6.2 22.6 0s6.2 16.4 0 22.6z"/></svg></i>
                
                <!-- deny button -->
                <i
                    role = "button" tabindex = {index} onclick={() => {
                        removeTell(index);
                    }}
                onkeydown={() => {}}>
                <svg class = "deny" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class:light-icon={!$theme} class:dark-icon={$theme}><path d="M367.2 412.5L99.5 144.8C77.1 176.1 64 214.5 64 256c0 106 86 192 192 192c41.5 0 79.9-13.1 111.2-35.5zm45.3-45.3C434.9 335.9 448 297.5 448 256c0-106-86-192-192-192c-41.5 0-79.9 13.1-111.2 35.5L412.5 367.2zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256z"/></svg></i>
            
            </div>
        </div>
        {/each}
    </main>
    <div class="enter-tell" style="width:80%;">
        <div class="mb-6" style="width:90%; margin-right:10px;">
            <input bind:value={currentTell} style="height:40px;" type="text" placeholder="  enter tell" id="default-input" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        </div>
        <button onclick={addTell} type="button" style="padding:10px; width:10%" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 me-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Dodaj</button>
    </div>
</div>



<style>
    *{
        transition: all .2s ease-in-out;
        overflow-x:hidden;
    }

    .wrapper{
        width: 100vw;
        display: flex;
        flex-direction: column;
        overflow: hidden; /* Prevent overflow */
        background-color: red;
        align-items: center;
    }

    main{
        flex:1;
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

    .telle-action-icons > i {
        width: 40px; /* Increase icon size */
        height: 40px; /* Increase icon size */
        padding: 5px; /* Adjust padding */
        cursor: pointer;
    }

    .telle-action-icons > i:hover {
        transform:scale(1.2);
        cursor: pointer;
    }

    .check{
        fill:green !important;
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

    .enter-tell {
        position: fixed;
        bottom: 20px;
        width: 100vw;
        display: flex;
        flex-direction: row;
        justify-content: center;
        background: white; /* Keep it visible when scrolling */
        padding: 10px;
        border-top: 2px solid #ccc; /* Optional: adds a divider */
    }
    

</style>
