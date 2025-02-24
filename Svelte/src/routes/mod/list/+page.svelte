<script lang="ts">
    import { theme } from "../../../stores";
    import { auth } from "../../../lib/firebase/firebase";
    import { signOut } from "firebase/auth";
    
    let telle = ["bajka", "jajko"];
    let currentTell = '';
    let error = false;
    let isEditing = false;
  
    function addTell() {
      error = false;
      if (!currentTell.trim()) {
        error = true;
        return;
      }
      telle = [...telle, currentTell];
      currentTell = "";
      isEditing = false;
    }
  
    function editTell(index) {
      if (isEditing) return;
      currentTell = telle[index];
      telle = telle.filter((_, i) => i !== index);
      isEditing = true;
    }
  
    function removeTell(index) {
      telle = telle.filter((_, i) => i !== index);
      if (isEditing) {
        currentTell = '';
        isEditing = false;
      }
    }
  
    function handleKeyPress(e) {
      if (e.key === 'Enter') {
        addTell();
      }
    }

    async function handleLogout() {
        try {
            await signOut(auth);
            window.location.href = "/";
        } catch (error) {
            console.log("Error signing out:", error);
        }
    }

  </script>
  
  <div class="wrapper" class:light-wrapper={!$theme} class:dark-wrapper={$theme}>
    <button 
      on:click={handleLogout}
      class="logout-button"
      class:light-button={!$theme}
      class:dark-button={$theme}
      >
      Logout
    </button>
    <main>
      <h1 class="title" class:light-text={!$theme} class:dark-text={$theme}>Telle: </h1>
      
      <div class="list-container">
        {#each telle as tell, index}
          <div 
            class="tell-item" 
            class:light-tell={!$theme} 
            class:dark-tell={$theme}
          >
            <div class="tell-content">
              <span class="tell-number">{index + 1}.</span>
              <p class="tell-text">{tell}</p>
            </div>
            
            <div class="tell-actions">
              <button
                class="action-btn check-btn"
                aria-label="Complete item"
              >
                <svg viewBox="0 0 512 512" class="icon">
                  <path d="M64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32zM337 209L209 337c-9.4 9.4-24.6 9.4-33.9 0l-64-64c-9.4-9.4-9.4-24.6 0-33.9s24.6-9.4 33.9 0l47 47L303 175c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9z"/>
                </svg>
              </button>
              
              <button
                class="action-btn edit-btn"
                on:click={() => editTell(index)}
                aria-label="Edit item"
                disabled={isEditing}
                class:disabled={isEditing}
              >
                <svg viewBox="0 0 512 512" class="icon">
                  <path d="M410.3 231l11.3-11.3-33.9-33.9-62.1-62.1L291.7 89.8l-11.3 11.3-22.6 22.6L58.6 322.9c-10.4 10.4-18 23.3-22.2 37.4L1 480.7c-2.5 8.4-.2 17.5 6.1 23.7s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L387.7 253.7 410.3 231zM160 399.4l-9.1 22.7c-4 3.1-8.5 5.4-13.3 6.9L59.4 452l23-78.1c1.4-4.9 3.8-9.4 6.9-13.3l22.7-9.1 0 32c0 8.8 7.2 16 16 16l32 0z"/>
                </svg>
              </button>
              
              <button
                class="action-btn delete-btn"
                on:click={() => removeTell(index)}
                aria-label="Delete item"
              >
                <svg viewBox="0 0 512 512" class="icon">
                  <path d="M367.2 412.5L99.5 144.8C77.1 176.1 64 214.5 64 256c0 106 86 192 192 192c41.5 0 79.9-13.1 111.2-35.5zm45.3-45.3C434.9 335.9 448 297.5 448 256c0-106-86-192-192-192c-41.5 0-79.9 13.1-111.2 35.5L412.5 367.2zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256z"/>
                </svg>
              </button>
            </div>
          </div>
        {/each}
      </div>
    </main>
  
    <div class="input-container" class:light-input-container={!$theme} class:dark-input-container={$theme}>
      <div class="input-wrapper">
        <input
          type="text"
          bind:value={currentTell}
          on:keypress={handleKeyPress}
          placeholder={isEditing ? "Edit item..." : "Add new item..."}
          class="input-field"
          class:error
          class:light-input={!$theme}
          class:dark-input={$theme}
        />
        {#if error}
          <p class="error-message">napisz tella</p>
        {/if}
      </div>
      <button 
        on:click={addTell}
        class="add-button"
        class:light-button={!$theme}
        class:dark-button={$theme}
      >
        {isEditing ? 'Save' : 'Add'}
      </button>
    </div>
  </div>
  
  <style>
    * {
      transition: all 0.2s ease-in-out;
      box-sizing: border-box;
    }
  
    .wrapper {
      height: calc(100vh - 50px);
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem 1rem;
      overflow:hidden;
    }
  
    .light-wrapper {
      background: linear-gradient(135deg, #f6f9fc 0%, #eef2f7 100%);
    }
  
    .dark-wrapper {
      background: linear-gradient(135deg, #1a1f2c 0%, #121620 100%);
    }
  
    main {
      width: 100%;
      max-width: 800px;
      margin: 0 auto;
      padding-bottom: 100px;
    }
  
    .title {
      font-size: 2.5rem;
      font-weight: 700;
      text-align: center;
      margin-bottom: 2rem;
    }
  
    .light-text {
      color: #1a1f2c;
    }
  
    .dark-text {
      color: #ffffff;
    }
  
    .list-container {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
  
    .tell-item {
      background: rgba(255, 255, 255, 0.8);
      backdrop-filter: blur(10px);
      border-radius: 12px;
      padding: 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
  
    .tell-item:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
  
    .light-tell {
      background: white;
      color: #1a1f2c;
    }
  
    .dark-tell {
      background: rgba(255, 255, 255, 0.1);
      color: white;
    }
  
    .tell-content {
      display: flex;
      align-items: center;
      gap: 1rem;
      flex: 1;
    }
  
    .tell-number {
      font-weight: 600;
      color: #6b7280;
      min-width: 2rem;
    }
  
    .tell-text {
      margin: 0;
      font-size: 1rem;
      line-height: 1.5;
    }
  
    .tell-actions {
      display: flex;
      gap: 0.5rem;
      opacity: 0.6;
      transition: opacity 0.2s ease;
    }
  
    .tell-item:hover .tell-actions {
      opacity: 1;
    }
  
    .action-btn {
      background: none;
      border: none;
      padding: 0.5rem;
      cursor: pointer;
      border-radius: 8px;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
    }
  
    .action-btn:hover:not(.disabled) {
      background-color: rgba(0, 0, 0, 0.05);
    }
  
    .action-btn.disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }
  
    .icon {
      width: 20px;
      height: 20px;
    }
  
    .check-btn .icon {
      fill: #10b981;
    }
  
    .edit-btn .icon {
      fill: #6366f1;
    }
  
    .delete-btn .icon {
      fill: #ef4444;
    }
  
    .input-container {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 1rem;
      display: flex;
      gap: 1rem;
      align-items: flex-start;
      max-width: 800px;
      margin: 0 auto;
      border-radius: 12px 12px 0 0;
    }
  
    .light-input-container {
      background: white;
      box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.05);
    }
  
    .dark-input-container {
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(10px);
    }
  
    .input-wrapper {
      flex: 1;
    }
  
    .input-field {
      width: 100%;
      padding: 0.75rem 1rem;
      border-radius: 8px;
      border: 2px solid transparent;
      font-size: 1rem;
      transition: all 0.2s ease;
    }
  
    .light-input {
      background: #f9fafb;
      color: #1a1f2c;
    }
  
    .dark-input {
      background: rgba(255, 255, 255, 0.05);
      color: white;
    }
  
    .input-field:focus {
      outline: none;
      border-color: #6366f1;
    }
  
    .input-field.error {
      border-color: #ef4444;
    }
  
    .error-message {
      color: #ef4444;
      font-size: 0.875rem;
      margin-top: 0.5rem;
    }
  
    .add-button {
      padding: 0.75rem 1.5rem;
      border-radius: 8px;
      border: none;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      min-width: 80px;
    }
  
    .light-button {
      background: #6366f1;
      color: white;
    }
  
    .dark-button {
      background: #818cf8;
      color: white;
    }
  
    .add-button:hover {
      transform: translateY(-1px);
      filter: brightness(1.1);
    }
  
    .add-button:active {
      transform: translateY(0);
    }
  
    @media (max-width: 640px) {
      .title {
        font-size: 2rem;
      }
  
      .input-container {
        padding: 1rem;
      }
  
      .tell-item {
        padding: 0.75rem;
      }
    }
    
    .logout-button {
        position: absolute;
        top: 20px;
        right: 20px;
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .logout-button:hover {
        transform: translateY(-1px);
        filter: brightness(1.1);
    }

    .logout-button:active {
        transform: translateY(0);
    }
  </style>