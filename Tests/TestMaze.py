import unittest
from Model.Maze import Maze
from Model.Room import Room
from Model.Pillar import PolymorphismPillar, AbstractionPillar, EncapsulationPillar, InheritancePillar
from Model.Potion import HealthPotion, VisionPotion
from Model.CharacterFactory import CharacterFactory
from Model.Element import Element


class TestMaze(unittest.TestCase):
    def setUp(self):
        Maze.delete_instance()  # Ensure fresh singleton instance for each test
        self.maze_size = 5
        self.maze = Maze(self.maze_size)

    def tearDown(self):
        Maze.delete_instance()  # Clean up singleton instance

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


    def test_set_and_get_array(self):
        custom_array = [[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)]
        self.maze.set_array(custom_array)
        self.assertEqual(self.maze.get_array(), custom_array)

if __name__ == "__main__":
    unittest.main()
