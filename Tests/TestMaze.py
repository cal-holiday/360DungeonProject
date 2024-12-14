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
        self.assertIsNone(Maze.get_instance())

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

    def test_check_neighbor_none(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        for i in range(len(self.maze.get_array())):
            for j in range(len(self.maze.room_array[i])):
                self.maze.room_array[i][j].set_has_visited(True)
        self.assertIsNone(self.maze.check_neighbors(self.maze.room_array[0][1]))

    def test_check_neighbor(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        neighbors = [self.maze.room_array[0][1], self.maze.room_array[0][1], self.maze.room_array[1][2], self.maze.room_array[2][1]]
        self.assertIn(self.maze.check_neighbors(self.maze.room_array[1][1]), neighbors)

    def remove_north_wall(self):
        self.maze.set_array([[Room(True, True, True, True, (x, y), None, None) for y in range(3)] for x in range(3)])
        self.maze.remove_walls(self.maze.room_array[1][1], self.maze.room_array[0][1])
        self.assertEqual(self.maze.room_array[1][1].get_nwall(), False)
        self.assertEqual(self.maze.room_array[0][1].get_swall(), False)

if __name__ == "__main__":
    unittest.main()
