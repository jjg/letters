
cube([20, 20, 40]);
translate([0.5, 0.5, 40]){
    linear_extrude(5){
        text("H", size=20);
    }
}
