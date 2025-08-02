"""
Tests para las nuevas funcionalidades de la Fase 2 (API Manager, Gamificación, etc.).
"""
import os
import unittest
from dashboard.app import app
from modules.gamification_manager import GamificationManager
from plugins.api_discovery_manager import ApiDiscoveryManager

class FeaturesTestCase(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de pruebas para cada test."""
        self.app = app.test_client()
        self.app.testing = True
        # Asegurarse de que los archivos de prueba no persistan
        if os.path.exists("gamification.db"):
            os.remove("gamification.db")
        if os.path.exists("api_config.json"):
            os.remove("api_config.json")

    def tearDown(self):
        """Limpia el entorno de pruebas después de cada test."""
        if os.path.exists("gamification.db"):
            os.remove("gamification.db")
        if os.path.exists("api_config.json"):
            os.remove("api_config.json")

    # --- Tests de Rutas del Dashboard ---

    def test_dashboard_routes(self):
        """Prueba que las nuevas rutas del dashboard carguen correctamente."""
        routes = ["/api-config", "/call-center", "/gamification", "/ai", "/ethics"]
        for route in routes:
            result = self.app.get(route)
            self.assertEqual(result.status_code, 200, f"La ruta {route} falló")

    # --- Tests del GamificationManager ---

    def test_gamification_manager(self):
        """Prueba la lógica del gestor de gamificación."""
        manager = GamificationManager()
        # Los datos de ejemplo se añaden en la creación
        leaderboard = manager.get_leaderboard()
        self.assertEqual(len(leaderboard), 2)
        self.assertEqual(leaderboard[0]['user_id'], 'bot_master_99')

        manager.add_points('api_wizard', 50)
        leaderboard = manager.get_leaderboard()
        self.assertEqual(leaderboard[0]['user_id'], 'api_wizard')
        self.assertEqual(leaderboard[0]['points'], 170)

    # --- Tests del ApiDiscoveryManager ---

    def test_api_manager(self):
        """Prueba la lógica del gestor de APIs."""
        manager = ApiDiscoveryManager()
        self.assertEqual(manager.get_all_configs(), {})

        # Probar añadir API manual
        manager.add_api_manual("TestService", "http://test.com", "12345")
        config = manager.get_api_config("TestService")
        self.assertIsNotNone(config)
        self.assertEqual(config['key'], '12345')

        # Probar flujo OAuth (simulado)
        manager.start_oauth_flow("Google")
        config = manager.get_api_config("Google")
        self.assertIsNotNone(config)
        self.assertIn("simulated_oauth_token", config['token'])

if __name__ == '__main__':
    unittest.main()
