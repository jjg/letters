
cube([20, 20, 40]);
translate([2, 0.5, 40]){
    linear_extrude(5){
        text("L", size=20);
    }
}
