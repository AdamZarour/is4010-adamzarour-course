# Rust Playground Exercise Links (Part 0)

This file contains Playground links for Part 0 of Lab 10, where you can experiment with Rust ownership and borrowing concepts in the browser.

## Recommended Exercises

Use the [Rust Playground](https://play.rust-lang.org/) to experiment with these concepts before working on the borrow checker game:

1. **Move semantics**
   - URL: [Add your Playground share link here]
   - Description: Understand how ownership moves when values are assigned or passed to functions

2. **Borrowing and references**
   - URL: [Add your Playground share link here]
   - Description: Practice immutable borrowing with `&T` references

3. **Mutable borrowing**
   - URL: [Add your Playground share link here]
   - Description: Understand mutable references `&mut T` and the one-mutable-or-many-immutable rule

4. **Ownership in functions**
   - URL: [Add your Playground share link here]
   - Description: Observe how ownership transfers through function parameters and return values

5. **String vs &str**
   - URL: [Add your Playground share link here]
   - Description: Experiment with owned Strings and borrowed string slices

## Additional Experiments

Feel free to add more Playground experiments here:

6. **Custom Exercise**
   - URL: [Add your Playground share link here]
   - Description: [Describe what you experimented with]

---

**Note**: These Playground exercises are optional but highly recommended for deepening your understanding of Rust's ownership system. The automated tests focus on your local Lab 10 implementation in `src/main.rs`.

## Key Concepts to Explore

- **The three ownership rules**: Each value has one owner, ownership can move, values are dropped when owners go out of scope
- **The two borrowing rules**: Either one mutable reference OR many immutable references, not both simultaneously
- **Lifetimes**: How long references are valid (implicit in most cases)
- **Ownership patterns**: Returning ownership, borrowing to avoid moves, cloning when needed
