// Letter B, 20x20x40

cube([20,20,40]);
translate([0,.5,40]){
    linear_extrude(5){
        text("B", size=20);
    }
}