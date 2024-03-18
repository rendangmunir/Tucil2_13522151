// document.getElementById("userForm").addEventListener("submit", function(event) {
//     event.preventDefault();
//     let userInput = document.getElementById("nameInput").value;
//     document.getElementById("message").textContent = "Hello, " + userInput + "!";
// });

// document.getElementById("control-points").addEventListener("submit", function(event) {
//     event.preventDefault();
//     let ctrl = document.getElementById("points").value;
//     console.log(ctrl);
// });

// let canvas = document.getElementById("canvas");

// canvas.width = window.innerWidth/2;
// canvas.height = window.innerHeight/2;

// const ctx = canvas.getContext("2d");

function BezierN(control_points, iter, mid_points, curve_points) {
    if (iter > 0) {
        let n = control_points.length - 1;
        let left = [...control_points].reverse();
        let right = [...control_points];
        curve_points.push(control_points[0]);
        while (n > 0) {
            for (let i = 0; i < n; i++) {
                right[i] = [(right[i][0] + right[i + 1][0]) * 0.5, (right[i][1] + right[i + 1][1]) * 0.5];
                left[i] = [(left[i][0] + left[i + 1][0]) * 0.5, (left[i][1] + left[i + 1][1]) * 0.5];
                mid_points.push(right[i]);
            }
            if (n === 1) {
                BezierLeft(left, iter - 1, mid_points, curve_points);
                curve_points.push(right[0]);
                BezierRight(right, iter - 1, mid_points, curve_points);
                curve_points.push(control_points[control_points.length - 1]);
            }
            n--;
        }
    }
}

function BezierLeft(control_points, iter, mid_points, curve_points) {
    if (iter > 0) {
        let n = control_points.length - 1;
        let left = [...control_points];
        let right = [...control_points].reverse();
        while (n > 0) {
            for (let i = 0; i < n; i++) {
                right[i] = [(right[i][0] + right[i + 1][0]) * 0.5, (right[i][1] + right[i + 1][1]) * 0.5];
                left[i] = [(left[i][0] + left[i + 1][0]) * 0.5, (left[i][1] + left[i + 1][1]) * 0.5];
                mid_points.push(right[i]);
            }
            if (n === 1) {
                BezierLeft(left, iter - 1, mid_points, curve_points);
                curve_points.push(left[0]);
                BezierRight(right, iter - 1, mid_points, curve_points);
            }
            n--;
        }
    }
}

function BezierRight(control_points, iter, mid_points, curve_points) {
    if (iter > 0) {
        let n = control_points.length - 1;
        let left = [...control_points].reverse();
        let right = [...control_points];
        while (n > 0) {
            for (let i = 0; i < n; i++) {
                right[i] = [(right[i][0] + right[i + 1][0]) * 0.5, (right[i][1] + right[i + 1][1]) * 0.5];
                left[i] = [(left[i][0] + left[i + 1][0]) * 0.5, (left[i][1] + left[i + 1][1]) * 0.5];
                mid_points.push(right[i]);
            }
            if (n === 1) {
                BezierLeft(left, iter - 1, mid_points, curve_points);
                curve_points.push(right[0]);
                BezierRight(right, iter - 1, mid_points, curve_points);
            }
            n--;
        }
    }
}

function drawCurve(curve_points) {
    const canvas = document.getElementById('canvas');
    canvas.width = window.innerWidth/2;
    canvas.height = window.innerHeight/2;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.moveTo(curve_points[0][0], curve_points[0][1]);
    for (let i = 1; i < curve_points.length; i++) {
        ctx.lineTo(curve_points[i][0], curve_points[i][1]);
    }
    ctx.stroke();
}

let control_points = [[200, 300], [300, 200], [0, 200], [100, 300]];
let curve_points = [];
let mid_points = [];
BezierN(control_points, 2, mid_points, curve_points);
console.log(curve_points);


drawCurve(curve_points);


