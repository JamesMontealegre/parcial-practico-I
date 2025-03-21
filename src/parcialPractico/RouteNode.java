package parcialPractico;

class RouteNode {
    String location;
    RouteNode next;

    public RouteNode(String location) {
        this.location = location;
        this.next = null;
    }
}