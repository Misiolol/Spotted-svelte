<script>
    import Authenticate from "../../components/authenticate.svelte";
    import { theme } from "../../stores";

</script>

<div class="wrapper" class:light-wrapper={!$theme} class:dark-wrapper={$theme}>
    <Authenticate />
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

</style>

