from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Counter to store the frequency of each letter in the tiles string
        tile_count = Counter(tiles)
        result = set()  # Set to store unique sequences

        def backtrack(sequence, tile_count):
            # If the sequence is non-empty, add it to the result set
            if sequence:
                result.add(sequence)

            # Try adding each tile to the sequence if available
            for tile in tile_count:
                if tile_count[tile] > 0:  # If this tile is still available
                    tile_count[tile] -= 1  # Use the tile
                    backtrack(sequence + tile, tile_count)  # Recurse with this tile added
                    tile_count[tile] += 1  # Backtrack (restore the tile count)

        # Start the backtracking process with an empty sequence
        backtrack("", tile_count)
        
        # The result set now contains all unique non-empty sequences
        return len(result)
