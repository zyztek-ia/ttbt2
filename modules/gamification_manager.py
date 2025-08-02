"""
Módulo de Gamificación.
Gestiona la base de datos de puntos y logros de los usuarios.
"""
import sqlite3
import os

DB_FILE = "gamification.db"

class GamificationManager:
    """Gestiona la lógica de la base de datos para la gamificación."""

    def __init__(self):
        """Inicializa el gestor y crea la tabla si no existe."""
        self._create_table()

    def _get_db_connection(self):
        """Establece conexión con la base de datos SQLite."""
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        return conn

    def _create_table(self):
        """Crea la tabla de 'leaderboard' si no existe."""
        conn = self._get_db_connection()
        # Check if table exists
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='leaderboard'")
        if cursor.fetchone() is None:
            # Table does not exist, create it and add data
            conn.execute(
                'CREATE TABLE leaderboard (user_id TEXT PRIMARY KEY, points INTEGER, achievements TEXT)'
            )
            # Añadir datos de ejemplo
            conn.execute(
                'INSERT INTO leaderboard (user_id, points, achievements) VALUES (?, ?, ?)',
                ('bot_master_99', 150, '["Primer Bot", "Integración API"]')
            )
            conn.execute(
                'INSERT INTO leaderboard (user_id, points, achievements) VALUES (?, ?, ?)',
                ('api_wizard', 120, '["Conexión OAuth"]')
            )
            conn.commit()
        conn.close()

    def add_points(self, user_id, points_to_add):
        """
        Añade puntos a un usuario. Si el usuario no existe, lo crea.
        :param user_id: El identificador del usuario.
        :param points_to_add: La cantidad de puntos a añadir.
        """
        self._create_table() # Asegurar que la tabla existe
        conn = self._get_db_connection()
        user = conn.execute('SELECT * FROM leaderboard WHERE user_id = ?', (user_id,)).fetchone()
        if user:
            new_points = user['points'] + points_to_add
            conn.execute('UPDATE leaderboard SET points = ? WHERE user_id = ?', (new_points, user_id))
        else:
            conn.execute('INSERT INTO leaderboard (user_id, points, achievements) VALUES (?, ?, ?)',
                         (user_id, points_to_add, '[]'))
        conn.commit()
        conn.close()

    def get_leaderboard(self, limit=10):
        """
        Obtiene el leaderboard ordenado por puntos.
        :param limit: El número máximo de usuarios a devolver.
        :return: Una lista de filas de la base de datos.
        """
        self._create_table() # Asegurar que la tabla existe
        conn = self._get_db_connection()
        leaderboard = conn.execute(
            'SELECT * FROM leaderboard ORDER BY points DESC LIMIT ?', (limit,)
        ).fetchall()
        conn.close()
        return leaderboard
