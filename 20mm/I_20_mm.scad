
cube([20, 20, 40]);
translate([6, 0.5, 40]){
    linear_extrude(5){
        text("I", size=20);
    }
}
