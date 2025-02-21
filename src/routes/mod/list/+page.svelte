<script>
    import { theme } from "../../../stores";
    import { telle } from "../../../stores";
    
</script>

<div class="wrapper" class:light-wrapper={!$theme} class:dark-wrapper={$theme}>
    <main>
        {#await $telle then data}
            {#each data as tell}
                <div class="tell" class:light-tell={!$theme} class:dark-tell={$theme}>
                    {tell}
                </div>
            {/each}
        {/await}
    
    </main>
</div>



<style>
    .wrapper{
        height: calc(100vh - 40px); /* Subtract header height (40px) */
        width: 100vw;
        display: flex;
        flex-direction: column;
        transition: all .2s ease-in-out;
        overflow: hidden; /* Prevent overflow */
        background-color: red;
        align-items: center;
        justify-content: center;
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
        transition: all .2s ease-in-out;
        border-left:1px solid cyan;
        padding:4px;
    }
</style>
