<script>
  import { authHandlers } from "../store/store";
  import { theme } from "../stores";

  let email = "";
  let password = "";
  let confirmPass = "";
  let error = false;
  let errorMessage = "";
  let register = false;
  let authenticating = false;

  async function handleAuthenticate(e) {
    e.preventDefault();
    if (authenticating) return;
    
    if (password.length < 6) {
        error = true;
        errorMessage = "Password must be at least 6 characters long";
        console.log(errorMessage);
        return;
    }

    if (!email || !password || (register && !confirmPass)) {
        error = true;
        errorMessage = "Please fill in all fields";
        console.log(errorMessage);
        return;
    }

    if (register && password !== confirmPass) {
        error = true;
        errorMessage = "Passwords do not match";
        console.log(errorMessage);
        return;
    }

    authenticating = true;

    try {
        if (!register) {
            await authHandlers.login(email, password);
        } else {
            await authHandlers.signup(email, password);
        }
    } catch (err) {
        console.log("There was an auth error", err);
        error = true;
        errorMessage = err.message;
    } finally {
        authenticating = false;
    }
  }

  function handleRegister() {
    register = !register;
    error = false;
    errorMessage = "";
    email = "";
    password = "";
    confirmPass = "";
  }
</script>

<div class="authContainer">
  <form on:submit|preventDefault={handleAuthenticate}>
    <h1 class:light-text={!$theme} class:dark-text={$theme}>{register ? "Register" : "Login"}</h1>
    {#if error}
      <p class="error">cos zle</p>
    {/if}
    <label>
      <p class:light-text={!$theme} class:dark-text={$theme} class={email ? "above" : "center"}>Email</p>
      <input class:light-text={!$theme} class:dark-text={$theme} bind:value={email} type="email" placeholder="Email" />
    </label>
    <label>
      <p class:light-text={!$theme} class:dark-text={$theme} class={password ? "above" : "center"}>Password</p>
      <input class:light-text={!$theme} class:dark-text={$theme} bind:value={password} type="password" placeholder="Password" />
    </label>
    {#if register}
      <label>
        <p class:light-text={!$theme} class:dark-text={$theme} class={confirmPass ? "above" : "center"}>Confirm Password</p>
        <input bind:value={confirmPass} type="password" placeholder="Confirm Password" />
      </label>
    {/if}

    <button type="submit" class="submitBtn">
      {#if authenticating}
        <i class="fa-solid fa-spinner loadingSpinner" />
      {:else}
        Submit
      {/if}
    </button>
  </form>
  <div class="options">
    {#if register}
      <div>
        <p>Already have an account?</p>
        <p on:click={handleRegister} on:keydown={() => {}}>Login</p>
      </div>
    {:else}
      <!--<div>
        <p>Don't have an account?</p>
        <p on:click={handleRegister} on:keydown={() => {}}>Register</p>
      </div>-->
    {/if}
  </div>
</div>

<style>
  .authContainer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex: 1;
    padding: 24px;
  }

  .light-text {
      color: #1a1f2c;
    }
  
  .dark-text {
    color: #ffffff;
    }

  form {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  form,
  .options {
    width: 400px;
    max-width: 100%;
    margin: 0 auto;
  }

  form input {
    width: 100%;
  }

  h1 {
    text-align: center;
    font-size: 3rem;
  }

  form label {
    position: relative;
    border: 1px solid navy;
    border-radius: 5px;
  }

  form input {
    border: none;
    background: transparent;
    color: white;
    padding: 14px;
  }

  form input:focus {
    border: none;
    outline: none;
  }

  form label:focus-within {
    border-color: blue;
  }

  form button {
    background: navy;
    color: white;
    border: none;
    padding: 14px 0;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    display: grid;
    place-items: center;
  }

  form button:hover {
    background: blue;
  }

  .above,
  .center {
    position: absolute;
    transform: translateY(-50%);
    pointer-events: none;
    color: white;
    border-radius: 4px;
    padding: 0 6px;
    font-size: 0.8rem;
  }

  .above {
    top: 0;
    left: 24px;
    background: navy;
    border: 1px solid blue;
    font-size: 0.7rem;
  }

  .center {
    top: 50%;
    left: 6px;
    border: 1px solid transparent;
    opacity: 0;
  }

  .error {
    color: coral;
    font-size: 0.9rem;
    text-align: center;
  }

  .options {
    padding: 14px 0;
    overflow: hidden;
    font-size: 0.9rem;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .options > p {
    position: relative;
    text-align: center;
    width: fit-content;
    margin: 0 auto;
    padding: 0 8px;
  }

  .options > p::after,
  .options > p::before {
    position: absolute;
    content: "";
    top: 50%;
    transform: translateY(-50%);
    width: 100vw;
    height: 1.5px;
    background: white;
  }

  .options > p::after {
    right: 100%;
  }

  .options > p::before {
    left: 100%;
  }

  .options div {
    display: flex;
    align-items: center;
    gap: 8px;
    justify-content: center;
  }

  .options div p:last-of-type {
    color: cyan;
    cursor: pointer;
  }

  .loadingSpinner {
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    from {
      transform: rotate(0deg);
    }
    to {
      transform: rotate(360deg);
    }
  }
</style>
