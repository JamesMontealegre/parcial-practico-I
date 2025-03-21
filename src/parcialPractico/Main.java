package parcialPractico;

public class Main {
    public static void main(String[] args) {
        String apellido = "COLMENARES";
        String codigo = "407946";
        int ultimoDigito = Character.getNumericValue(codigo.charAt(codigo.length() - 1));

        String[] locations = {
                "Avenida Central",
                "Calle 5",
                "Plaza Mayor",
                "Avenida del Río",
                "Estación Norte",
                "Parque Sur",
                "Museo Nacional",
                "Teatro Municipal",
                "Universidad Central",
                "Biblioteca Pública"
        };

        Route cityRoute = new Route();

        for (int i = 0; i < locations.length; i++) {
            if ((ultimoDigito % 2 == 0 && i % 2 == 0) || (ultimoDigito % 2 != 0 && i % 2 != 0)) {
                cityRoute.addLocation(locations[i]);
            }
        }

        cityRoute.showRoute();
        System.out.println("\n🔄 Simulación del recorrido en la ruta:\n");
        cityRoute.navigateRoute();
    }
}