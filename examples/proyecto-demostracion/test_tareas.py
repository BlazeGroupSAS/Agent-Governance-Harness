import unittest
from tareas import agregar_tarea


class TareasTests(unittest.TestCase):
    def test_crea_pendiente(self):
        self.assertEqual(agregar_tarea([], " Comprar "), [{"titulo": "Comprar", "estado": "pendiente"}])

    def test_no_muta_lista_original(self):
        previas = [{"titulo": "A", "estado": "pendiente"}]
        nuevas = agregar_tarea(previas, "B")
        self.assertEqual(len(previas), 1)
        self.assertEqual([x["titulo"] for x in nuevas], ["A", "B"])

    def test_rechaza_blancos(self):
        for titulo in ["", "   ", "\t"]:
            with self.subTest(titulo=titulo), self.assertRaises(ValueError):
                agregar_tarea([], titulo)

    def test_rechaza_no_texto(self):
        for titulo in [None, 12, []]:
            with self.subTest(titulo=titulo), self.assertRaises(ValueError):
                agregar_tarea([], titulo)

    def test_lista_invalida(self):
        with self.assertRaises(TypeError):
            agregar_tarea({}, "A")


if __name__ == "__main__":
    unittest.main()
