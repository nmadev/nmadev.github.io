// document.addEventListener('DOMContentLoaded', function() {
//     const toggle = document.getElementById('toggle');
//     const body = document.body;

//     toggle.addEventListener('input', e => {
//         console.log("CHECKED\n");
//         const isChecked = e.target.checked;
    
//         if (isChecked) {
//             body.classList.add('dark-theme');
//         } else {
//             body.classList.remove('dark-theme');
//         }
//     });
// });



// Path: Website\nmadev.github.io\script.js



document.addEventListener('DOMContentLoaded', loaded);

function loaded() {
    // dark mode toggle
    const toggle = document.getElementById('toggle');
    const body = document.body;
    let darkMode = localStorage.getItem("dark-mode");
    console.log(darkMode);

    const enableDarkMode = () => {
        body.classList.add('dark-theme');
        localStorage.setItem("dark-mode", "enabled");
    };

    const disableDarkMode = () => {
        body.classList.remove('dark-theme');
        localStorage.setItem("dark-mode", "disabled");
    };

    const event = new Event('input');
    toggle.addEventListener('input', e => {
        let darkMode = localStorage.getItem("dark-mode");
        if (darkMode === "enabled") {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });

    if (darkMode === "enabled")
    {
        toggle.click();
        enableDarkMode();
    }
}

