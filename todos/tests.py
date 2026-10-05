from django.test import TestCase

from .models import Todo


class TodoModelTests(TestCase):
    """Pruebas unitarias del modelo Todo."""

    def test_str_devuelve_el_titulo(self):
        todo = Todo.objects.create(title="Comprar leche")
        self.assertEqual(str(todo), "Comprar leche")

    def test_tarea_nueva_no_esta_completada(self):
        todo = Todo.objects.create(title="Estudiar Git")
        self.assertFalse(todo.isCompleted)

    def test_fecha_de_creacion_se_asigna_automaticamente(self):
        todo = Todo.objects.create(title="Hacer el informe")
        self.assertIsNotNone(todo.created_at)