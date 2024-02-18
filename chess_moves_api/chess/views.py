# chess/views.py
import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


@csrf_exempt
def chess_moves(request, slug):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Implement logic to determine valid moves based on 'data' and 'slug'
            valid_moves = get_valid_moves(data, slug)
            logger.info(f"Valid moves for {slug}: {valid_moves}")
            return JsonResponse({'valid_moves': list(valid_moves)})
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            return JsonResponse({'error': 'An error occurred while processing the request'}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are supported'}, status=405)


def get_valid_moves(input_dict, piece_name):
    positions = input_dict.get("positions", {})
    all_possible_pieces_moves = {}
    for key_name, key_position in positions.items():
        if key_position is None:
            return {"valid_moves": set()}

        file_to_num = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        piece_file, piece_rank = key_position[0].lower(), int(key_position[1])
        x, y = file_to_num.get(piece_file), piece_rank

        if x is None:
            return {"valid_moves": set()}

        valid_moves = set()
        file_num_to_char = {v: k for k, v in file_to_num.items()}

        if key_name == "Knight":
            possible_moves = [
                (x + 1, y + 2), (x + 2, y + 1),
                (x + 2, y - 1), (x + 1, y - 2),
                (x - 1, y - 2), (x - 2, y - 1),
                (x - 2, y + 1), (x - 1, y + 2)
            ]
            valid_moves.update(
                file_num_to_char[move[0]] + str(move[1])
                for move in possible_moves
                if 1 <= move[0] <= 8 and 1 <= move[1] <= 8
            )

        elif key_name in ["Queen", "Bishop", "Rook"]:
            if key_name == "Queen":
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
            elif key_name == "Bishop":
                directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            else:  # Rook
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                for i in range(1, 8):
                    new_x, new_y = x + dx * i, y + dy * i
                    if 1 <= new_x <= 8 and 1 <= new_y <= 8:
                        valid_moves.add(file_num_to_char[new_x] + str(new_y))
                    else:
                        break

        all_possible_pieces_moves[key_name] = {"valid_moves": valid_moves}

    return get_distinct_valid_moves(all_possible_pieces_moves, piece_name)


def get_distinct_valid_moves(all_valid_moves, piece_name):
    piece_valid_moves = all_valid_moves[piece_name]['valid_moves']

    other_valid_moves = set()
    for piece, data in all_valid_moves.items():
        if piece != piece_name:
            other_valid_moves.update(data['valid_moves'])

    distinct_moves = piece_valid_moves - other_valid_moves

    return distinct_moves

