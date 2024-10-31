document.addEventListener("DOMContentLoaded", function() {
    const changeColorButton = document.getElementById("changeColorButton");
    const toggleVisibilityButton = document.getElementById("toggleVisibilityButton");
    const box = document.getElementById("box");

    changeColorButton.addEventListener("click", function() {
        console.log("clicked");
        // Generate a random color
        const randomColor = '#' + Math.floor(Math.random()*16777215).toString(16);
        box.style.backgroundColor = randomColor;
    });

    toggleVisibilityButton.addEventListener("click", function() {
        // Toggle the visibility of the box
        if (box.style.opacity === "0") {
            box.style.opacity = "1";
        } else {
            box.style.opacity = "0";
        }
    });
});
