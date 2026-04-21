document.addEventListener('DOMContentLoaded', function () {
  const body = document.body;
  const themeToggle = document.getElementById('theme-toggle');
  const formatBtn = document.getElementById('formatBtn');
  const formatMenu = document.getElementById('formatMenu');
  const formatInput = document.getElementById('formatInput');
  const downloadForm = document.getElementById('downloadForm');
  const urlInput = document.getElementById('urlInput');

  if (!body) return;

  // Initialize theme
  const savedTheme = localStorage.getItem('theme') || 'dark';
  body.setAttribute('data-theme', savedTheme);

  function updateThemeIcon() {
    if (!themeToggle) return;
    const theme = body.getAttribute('data-theme');
    // icon visibility is handled by CSS (two icons inside the button)
    themeToggle.setAttribute('aria-pressed', theme === 'dark');
    themeToggle.setAttribute('title', theme === 'dark' ? 'Ativar tema claro' : 'Ativar tema escuro');
  }
  updateThemeIcon();

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const next = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      body.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateThemeIcon();
    });
  }

  // Dropdown behavior
  let open = false;
  if (formatBtn && formatMenu) {
    formatBtn.addEventListener('click', function (e) {
      open = !open;
      formatMenu.style.display = open ? 'flex' : 'none';
      formatBtn.setAttribute('aria-expanded', open);
      formatMenu.setAttribute('aria-hidden', !open);
    });

    // Choose format
    const formatBtnIcon = formatBtn.querySelector('.btn-icon');
    const formatBtnLabel = formatBtn.querySelector('.format-label');

    Array.from(formatMenu.querySelectorAll('.format-option')).forEach(function (btn) {
      btn.addEventListener('click', function () {
        const f = btn.dataset.format || 'mp4';
        const label = btn.dataset.label || (btn.querySelector('.opt-label') && btn.querySelector('.opt-label').textContent) || 'MP4';
        if (formatInput) formatInput.value = f;
        if (formatBtnLabel) formatBtnLabel.textContent = label;
        const optIcon = btn.querySelector('.opt-icon');
        if (formatBtnIcon && optIcon) formatBtnIcon.innerHTML = optIcon.innerHTML;
        open = false;
        formatMenu.style.display = 'none';
        formatBtn.setAttribute('aria-expanded', false);
        formatMenu.setAttribute('aria-hidden', true);
      });
    });

    // close on outside click
    document.addEventListener('click', function (e) {
      if (!formatBtn.contains(e.target) && !formatMenu.contains(e.target)) {
        open = false;
        formatMenu.style.display = 'none';
        formatBtn.setAttribute('aria-expanded', false);
        formatMenu.setAttribute('aria-hidden', true);
      }
    });
  }

  // submit handling
  if (urlInput) {
    urlInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        const downloadBtn = document.getElementById('downloadBtn');
        if (downloadBtn) {
            downloadBtn.click(); // Trigger the modal logic instead of submitting
        } else if (downloadForm) {
            downloadForm.submit();
        }
      }
    });
  }

  if (downloadForm) {
    downloadForm.addEventListener('submit', function () {
      if (formatInput && !formatInput.value) formatInput.value = 'mp4';
    });
  }

  // --- Auth Flow --- //
  const loginBtnTrigger = document.getElementById('loginBtnTrigger');
  const loginDropdown = document.getElementById('loginDropdown');
  const openSignupModal = document.getElementById('openSignupModal');
  const signupModal = document.getElementById('signupModal');
  const closeSignupModal = document.getElementById('closeSignupModal');
  const cancelSignup = document.getElementById('cancelSignup');

  if (loginBtnTrigger && loginDropdown) {
    console.log("Auth setup ok!");
    // Toggle dropdown on click
    loginBtnTrigger.addEventListener('click', function (e) {
      e.stopPropagation();
      console.log("Login dropdown clicado!");
      loginDropdown.classList.toggle('show');
    });

    // Prevent closing when clicking inside the dropdown
    loginDropdown.addEventListener('click', function (e) {
      e.stopPropagation();
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function() {
      if (loginDropdown.classList.contains('show')) {
        loginDropdown.classList.remove('show');
      }
    });
  }

  // Open Signup Modal
  if (openSignupModal && signupModal) {
    openSignupModal.addEventListener('click', function (e) {
      e.preventDefault();
      // Hide the login dropdown when opening modal
      loginDropdown.classList.remove('show');
      
      // Open the signup modal exactly like the format modal logic
      signupModal.classList.add('active');
      document.body.classList.add('modal-open');
    });
  }

  // Close Signup Modal
  function closeSignUp() {
    if (signupModal) {
      signupModal.classList.remove('active');
      document.body.classList.remove('modal-open');
    }
  }

  if (closeSignupModal) closeSignupModal.addEventListener('click', closeSignUp);
  if (cancelSignup) cancelSignup.addEventListener('click', closeSignUp);
  
  // --- Avatar Upload Preview --- //
  const avatarUploadContainer = document.getElementById('avatarUploadContainer');
  const avatarInput = document.getElementById('avatarInput');
  const avatarPreview = document.getElementById('avatarPreview');

  if (avatarUploadContainer && avatarInput && avatarPreview) {
    avatarUploadContainer.addEventListener('click', function() {
      avatarInput.click();
    });

    avatarInput.addEventListener('change', function(e) {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
          avatarPreview.src = e.target.result;
        }
        reader.readAsDataURL(file);
      }
    });
  }

});
