const canvas = document.getElementById('tree');
const generateButton = document.getElementById('generate-button');
const context = canvas.getContext('2d');

let angleParameter;
let recursionParameter;
let widthParameter;
let barkColor;
let leafColor;

function setAngleParameter(){
    angleParameter = +document.getElementById("angle_parameter").value;
}

function setRecursionParameter(){
    recursionParameter = +document.getElementById("recursion_parameter").value;
}

function setWidthParametr(){
    widthParameter  = +document.getElementById("width_parameter").value;
}

function setBarkColor(){
    barkColor  = document.getElementById("bark-color").value;
}

function setLeafColor(){
    leafColor  = document.getElementById("leaf-color").value;
}

function drawTree(recursion_depth, start_x, start_y, len, angle, angle_parameter, branchWidth, color1, color2){

    if (branchWidth <= 0){
        branchWidth = 1
    }

    context.beginPath();
    context.save();
    context.strokeStyle = color1;
    context.fillStyle = color2;
    context.lineWidth = branchWidth;
    context.translate(start_x,start_y);
    context.rotate(angle * Math.PI/100);
    context.moveTo(0,0);
    context.lineTo(0,-len);
    context.stroke();

    if (recursion_depth < 1)  {
        context.beginPath()
        context.arc(0,-len, 10,0, Math.PI/2);
        context.fill();

        context.beginPath()
        context.arc(0,-len, 10, Math.PI/2, Math.PI);
        context.fill();

        context.restore();

        return;
    }

    drawTree(recursion_depth-1, 0, -len, len * 0.75, angle + angle_parameter, angle_parameter, branchWidth -1);
    drawTree(recursion_depth-1, 0, -len, len * 0.75, angle - angle_parameter, angle_parameter, branchWidth - 1);


    context.restore();
}

generateButton.addEventListener('click',()=>{
    context.clearRect(0, 0, canvas.width, canvas.height);
    drawTree(recursionParameter, 250, 700, 150, 0, angleParameter, widthParameter, barkColor, leafColor);})
