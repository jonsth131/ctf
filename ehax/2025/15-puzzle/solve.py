import heapq
import requests
import re
import base64

class PuzzleSolver:
    def __init__(self, puzzle):
        self.goal_state = (
            (1, 2, 3, 4),
            (5, 6, 7, 8),
            (9, 10, 11, 12),
            (13, 14, 15, 0)
        )
        self.start_state = tuple(tuple(row) for row in puzzle)
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def find_zero(self, state):
        for r in range(4):
            for c in range(4):
                if state[r][c] == 0:
                    return r, c

    def manhattan_distance(self, state):
        distance = 0
        for r in range(4):
            for c in range(4):
                val = state[r][c]
                if val != 0:
                    goal_r, goal_c = (val - 1) // 4, (val - 1) % 4
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    def generate_next_states(self, state, reverse=False):
        zero_r, zero_c = self.find_zero(state)
        next_states = []
        state_list = [list(row) for row in state]

        for dr, dc in (self.moves[::-1] if reverse else self.moves):  # Reverse moves for backward search
            new_r, new_c = zero_r + dr, zero_c + dc
            if 0 <= new_r < 4 and 0 <= new_c < 4:
                state_list[zero_r][zero_c], state_list[new_r][new_c] = state_list[new_r][new_c], state_list[zero_r][zero_c]
                next_states.append((tuple(tuple(row) for row in state_list), [dr, dc]))
                state_list[zero_r][zero_c], state_list[new_r][new_c] = state_list[new_r][new_c], state_list[zero_r][zero_c]

        return next_states

    def bidirectional_solve(self):
        """Solve the 15-puzzle using a Corrected Bidirectional A* Search."""
        forward_queue = []
        backward_queue = []

        forward_visited = {}
        backward_visited = {}

        g_start = 0
        g_goal = 0

        h_start = self.manhattan_distance(self.start_state)
        h_goal = 0  # Goal state heuristic is always 0

        heapq.heappush(forward_queue, (h_start + g_start, g_start, self.start_state, []))
        heapq.heappush(backward_queue, (h_goal + g_goal, g_goal, self.goal_state, []))

        while forward_queue and backward_queue:
            # Expand forward search
            _, g_f, state_f, path_f = heapq.heappop(forward_queue)

            if state_f in backward_visited:
                return path_f + [(-dr, -dc) for dr, dc in reversed(backward_visited[state_f])]

            forward_visited[state_f] = path_f

            for next_state, move in self.generate_next_states(state_f):
                if next_state in forward_visited:
                    continue
                new_path = path_f + [move]
                new_g = g_f + 1
                new_h = self.manhattan_distance(next_state)
                heapq.heappush(forward_queue, (new_g + new_h, new_g, next_state, new_path))

            # Expand backward search
            _, g_b, state_b, path_b = heapq.heappop(backward_queue)

            if state_b in forward_visited:
                return forward_visited[state_b] + [(-dr, -dc) for dr, dc in reversed(path_b)]

            backward_visited[state_b] = path_b

            for next_state, move in self.generate_next_states(state_b, reverse=True):
                if next_state in backward_visited:
                    continue
                new_path = path_b + [move]
                new_g = g_b + 1
                new_h = self.manhattan_distance(next_state)
                heapq.heappush(backward_queue, (new_g + new_h, new_g, next_state, new_path))

        return None  # No solution found

path = "/p/d7b51dadf6594b0e8e0737a88ea176fd"

s = requests.Session()

while True:
    next_url = f"http://chall.ehax.tech:8001{path}"
    data = s.get(next_url)

    puzzle_data = re.search(r'let puzzle = (\[\[.*\]\]);', data.text).group(1)

    print("Found puzzle for path", path)
    puzzle = eval(puzzle_data)
    solver = PuzzleSolver(puzzle)
    solution = solver.bidirectional_solve()
    print(solution)

    response = s.post(f"{next_url}/check", json={"movements": solution})

    if response.json()["solved"] == True:
        print("Solved puzzle!")
        print(response.json())
        path = response.json()["next_puzzle"]
    else:
        print("Failed to solve puzzle!")
        print(response.json())
        break

    if not path.startswith("/p/"):
        response = s.get(f"http://chall.ehax.tech:8001{path}")
        print(base64.b64decode(response.headers["Hmm"]).decode())
        break

