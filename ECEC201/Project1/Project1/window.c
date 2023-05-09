#include "house.h"
#include <stdio.h>
#include <string.h>
/*converts choice to x,y*/
void choice_to_xy(int choice, int *xbuf, int *ybuf)
{
  *xbuf = (choice + 2) % 3;
  *ybuf = (choice - 1) / 3;
}
/* Updates the graphics for the window @ coordinates (x, y) to match the
 * `state` array.
 *
 *   This function modifies the `house` array by updating the characters
 *   inside the window located at the zero indexed coordinates (x, y) to
 *   match the window's state in the `state` array.  If the window's
 *   state is 1, then the window is filled with the '#' character.
 *   Likewise, if the window's state is 0 in the `state` array, the
 *   window is filled with the ' ' character.
 *
 * Parameters:
 *   house -- pointer to characters representing the house
 *
 *   state -- pointer to the game state array
 *
 *       x -- the horizontal coordinate of the window for which the
 *            state will be updated (zero indexed, with 0 being
 *            the left column and 2 being the right column)
 *
 *       y -- the vertical coordinate of the window for which the
 *            state will be updated (zero indexed, with 0 being
 *            the top row and 2 being the bottom row)
 */
void window_update_graphics(char *house, const int *state, int x, int y)
{
  int val = state[3 * y + x];
  int special_y[] = {8, 14, 20};
  int special_x[] = {11, 29, 47};
  int window_width = 11;
  int window_height = 3;
  int idx, idy;
  house[special_y[y] * HOUSE_WIDTH + special_x[x]] = val ? '#' : ' ';

  for (idy = 0; idy < window_height; idy++)
  {
    for (idx = 0; idx < window_width; idx++)
    {
      house[(special_y[y] + idy) * HOUSE_WIDTH + (special_x[x] + idx)] = val ? '#' : ' ';
    }
  }
}

/* Toggles the state of the window @ coordinates (x, y) in the game
 * state array.
 *
 *   This function modifies the `state` array by toggling the value
 *   corresponding to the window at the provided coordinates (x, y).  If
 *   the current value is 1, then it will be toggled to 0.  Likewise, if
 *   the current value is 0, then it will be toggled to 1.
 *
 * Parameters:
 *   state -- pointer to the game state array
 *
 *       x -- the horizontal coordinate of the window for which the
 *            state will be updated (zero indexed, with 0 being
 *            the left column and 2 being the right column)
 *
 *       y -- the vertical coordinate of the window for which the
 *            state will be updated (zero indexed, with 0 being
 *            the top row and 2 being the bottom row)
 */
void window_toggle_state(int *state, int x, int y)
{
  state[y * 3 + x] = state[y * 3 + x] ? 0 : 1;
}

/* Toggles the state and, correspondingly, updates the graphics for the
 * window @ coordinates (x, y).
 *
 *   Given the zero indexed coordinates (x, y) of a window, this
 *   function ensures that the corresponding element in the game state
 *   array is toggled appropriately and that the graphics corresponding
 *   to that window are updated appropriately to reflect the new state.
 *
 *   Hint: call other functions you have written to make this easier.
 *
 * Parameters:
 *   state -- pointer to the game state array
 *
 *   house -- pointer to characters representing the house
 *
 *       x -- the horizontal coordinate of the window for which the
 *            state will be updated (zero indexed, with 0 being
 *            the left column and 2 being the right column)
 *
 *       y -- the vertical coordinate of the window for which the
 *            state will be updated (zero indexed, with 0 being
 *            the top row and 2 being the bottom row)
 */
void window_update(int *state, char *house, int x, int y)
{
  window_update_graphics(house, state, x, y);
}

/* Toggles the lights based on the user's window selection.
 *
 *   Given the user's choice of window number, this function updates the
 *   corresponding window's (or windows') state and graphics, as
 *   necessary.
 *
 *   Hints:
 *     -- A primary job of this function will be to convert the choice
 *        of the user into the zero indexed (x, y) coordinates of a
 *        window.
 *
 *     -- Converting between `choice` and the (x, y) coordinates will
 *        probably be easier if you internally number the windows
 *        starting at zero (i.e. 0 thru 8 instead of 1 thru 9).
 *
 *     -- This function will need to call one other function
 *        (perhaps multiple times).
 *
 *   For Step 2, this function will only toggle the window
 *   corresponding to the user's selection.
 *
 *   For Step 3, this function will toggle the selected window
 *   and its neighbors (as described above in the instructions).
 *
 * Parameters:
 *    state -- pointer to the game state array
 *
 *    house -- pointer to characters representing the house
 *
 *   choice -- integer corresponding to the user's window selection
 *             (an integer value within the range 1 to 9)
 */
void window_toggle(int *state, char *house, int choice)
{
  /* Step 2: Write this function! (for single window toggle) */
  int x, y, xbuf, ybuf;
  choice_to_xy(choice, &x, &y);
  window_toggle_state(state, x, y);
  window_update(state,house,x,y);
  int i;
  for (i = 0; i < 9; i++)
  {
    choice_to_xy(i+1 , &xbuf, &ybuf);
    if ((x - 1 == xbuf || x + 1 == xbuf) && y == ybuf)
    {
      /*printf("toggel %d,%d\n", xbuf, ybuf);*/
      window_toggle_state(state, xbuf, ybuf);
      window_update(state, house, xbuf, ybuf);
    }
    if ((y - 1 == ybuf || y + 1 == ybuf) && (x == xbuf))
    {
      /*printf("toggel %d,%d\n", xbuf, ybuf);*/
      window_toggle_state(state, xbuf, ybuf);
      window_update(state, house, xbuf, ybuf);
    }
  }

  /* Step 3: Rewrite this function! (for multi-window toggle) */
}
