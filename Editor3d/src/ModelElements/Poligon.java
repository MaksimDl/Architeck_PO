package ModelElements;

import Service.Point3D;

import java.util.ArrayList;
import java.util.List;

public class Poligon {

    public Poligon() {  // т.к. композиция, то извне не приходит - все гибнет вместе с классом при удалении.
       this.points =  new ArrayList<>();
       points.add(new Point3D());  // минимум 1 элемент  добавить(1.*)
    }

    public List<Point3D> points;
}
