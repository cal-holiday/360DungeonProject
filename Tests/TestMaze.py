import unittest

from Model.Dungeon import Dungeon
from Model.Maze import Maze
from Model.Room import Room
from Model.Pillar import PolymorphismPillar, AbstractionPillar, EncapsulationPillar, InheritancePillar
from Model.Potion import HealthPotion, VisionPotion
from Model.CharacterFactory import CharacterFactory
from Model.Element import Element


class TestMaze(unittest.TestCase):
    def setUp(self):
        Maze.delete_instance()
        Dungeon.delete_instance() # Ensure fresh singleton instance for each test
        self.maze_size = 5
        self.maze = Maze(self.maze_size)

    def test_singleton_enforcement(self):
        with self.assertRaises(Exception) as context:
            Maze(self.maze_size)
        self.assertEqual(str(context.exception), "Dungeon already exists!")

    def test_get_instance(self):
        self.assertEqual(Maze.get_instance(), self.maze)

    def test_delete_instance(self):
        Maze.delete_instance()
        new_maze = Maze(self.maze_size)
        self.assertNotEqual(self.maze, new_maze)

    def test_maze_size_and_initialization(self):
        self.assertEqual(len(self.maze.get_array()), self.maze_size)
        for row in self.maze.get_array():
            self.assertEqual(len(row), self.maze_size)
            for room in row:
                self.assertIsInstance(room, Room)

    def test_maze_is_fully_connected(self):
        """
        Verify that the generated maze is fully connected, meaning all rooms
        are reachable from the starting room.
        """
        visited = set()

        def dfs(room):
            """
            Depth-first search to traverse the maze and mark all reachable rooms.
            """
            if room in visited:
                return
            visited.add(room)
            location = room.get_location()
            col, row = location
            if not room.get_nwall() and row > 0:
                dfs(self.maze.get_array()[col][row - 1])
            if not room.get_swall() and row < self.maze_size - 1:
                dfs(self.maze.get_array()[col][row + 1])
            if not room.get_wwall() and col > 0:
                dfs(self.maze.get_array()[col - 1][row])
            if not room.get_ewall() and col < self.maze_size - 1:
                dfs(self.maze.get_array()[col + 1][row])

        start_room = self.maze.get_array()[0][0]
        dfs(start_room)
        total_rooms = self.maze_size * self.maze_size
        self.assertEqual(len(visited), total_rooms, "Not all rooms are accessible in the maze.")

    def test_all_rooms_accessible(self):
        """
        Ensures all rooms are accessible in the generated maze.
        """
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            location = room.get_location()
            col, row = location
            # Check neighbors and traverse through open walls
            if not room.get_nwall() and row > 0:  # North wall is open
                dfs(self.maze.get_array()[col][row - 1])
            if not room.get_swall() and row < self.maze_size - 1:  # South wall is open
                dfs(self.maze.get_array()[col][row + 1])
            if not room.get_wwall() and col > 0:  # West wall is open
                dfs(self.maze.get_array()[col - 1][row])
            if not room.get_ewall() and col < self.maze_size - 1:  # East wall is open
                dfs(self.maze.get_array()[col + 1][row])

        # Start DFS from the top-left corner
        start_room = self.maze.get_array()[0][0]
        dfs(start_room)

        # Verify that all rooms were visited
        total_rooms = self.maze_size * self.maze_size
        self.assertEqual(len(visited), total_rooms, "Not all rooms are accessible in the maze.")

    def test_walls_removed_correctly(self):
        """
        Verifies that when two rooms are connected, their respective walls are removed.
        """
        for col in range(self.maze_size):
            for row in range(self.maze_size):
                current_room = self.maze.get_array()[col][row]
                # Check neighbors and verify wall consistency
                if row > 0:  # North neighbor
                    north_room = self.maze.get_array()[col][row - 1]
                    self.assertEqual(
                        current_room.get_nwall(), north_room.get_swall(),
                        f"Inconsistent walls between room at {current_room.get_location()} and north neighbor."
                    )
                if row < self.maze_size - 1:  # South neighbor
                    south_room = self.maze.get_array()[col][row + 1]
                    self.assertEqual(
                        current_room.get_swall(), south_room.get_nwall(),
                        f"Inconsistent walls between room at {current_room.get_location()} and south neighbor."
                    )
                if col > 0:  # West neighbor
                    west_room = self.maze.get_array()[col - 1][row]
                    self.assertEqual(
                        current_room.get_wwall(), west_room.get_ewall(),
                        f"Inconsistent walls between room at {current_room.get_location()} and west neighbor."
                    )
                if col < self.maze_size - 1:  # East neighbor
                    east_room = self.maze.get_array()[col + 1][row]
                    self.assertEqual(
                        current_room.get_ewall(), east_room.get_wwall(),
                        f"Inconsistent walls between room at {current_room.get_location()} and east neighbor."
                    )

    def test_set_and_get_array(self):
        custom_array = [[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)]
        self.maze.set_array(custom_array)
        self.assertEqual(self.maze.get_array(), custom_array)


if __name__ == "__main__":
    unittest.main()
