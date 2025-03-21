package parcialPractico;

class Route {
    private RouteNode head;

    public void addLocation(String location) {
        RouteNode newNode = new RouteNode(location);
        if (head == null) {
            head = newNode;
        } else {
            RouteNode current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    public void showRoute() {
        RouteNode current = head;
        if (current == null) {
            System.out.println("⚠️ No hay una ruta definida.");
            return;
        }
        System.out.println("🛣️ Ruta definida:");
        while (current != null) {
            System.out.println("➡️ " + current.location);
            current = current.next;
        }
    }

    public void navigateRoute() {
        RouteNode current = head;
        if (current == null) {
            System.out.println("⚠️ No hay una ruta para navegar.");
            return;
        }
        System.out.println("🚗 Iniciando recorrido...");
        showNextStep(current);
    }

    private void showNextStep(RouteNode node) {
        if (node == null) {
            System.out.println("🏁 Fin del recorrido.");
            return;
        }
        try {
            Thread.sleep(1500);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("🛑 Llegaste a: " + node.location);
        showNextStep(node.next);
    }
}