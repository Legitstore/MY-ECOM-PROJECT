const MainImg = document.getElementById('MainImg');
const smallimg = document.querySelectorAll('.small-img');

smallimg.forEach((img, index) => {
    img.onclick = function () {
        MainImg.src = this.src;
    }
});