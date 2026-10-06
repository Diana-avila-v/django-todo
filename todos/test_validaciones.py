from django.test import TestCase
from django.urls import reverse

from .models import Todo


class AgregarTareaTests(TestCase):
    """Pruebas de la validación del título al agregar una tarea."""

    def test_titulo_valido_crea_la_tarea(self):
        self.client.post(reverse('todos:add'), {'title': 'Estudiar Git'})
        self.assertEqual(Todo.objects.count(), 1)

    def test_titulo_vacio_no_crea_la_tarea(self):
        self.client.post(reverse('todos:add'), {'title': ''})
        self.assertEqual(Todo.objects.count(), 0)

    def test_titulo_solo_espacios_no_crea_la_tarea(self):
        self.client.post(reverse('todos:add'), {'title': '    '})
        self.assertEqual(Todo.objects.count(), 0)

    def test_sin_campo_titulo_no_genera_error(self):
        respuesta = self.client.post(reverse('todos:add'), {})
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)