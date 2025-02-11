# PyPokr
Abstracts over as many consumed APIs as possible (eventually...)

## System Architecture
- [x] Core
- [x] Menu Navigation
- [ ] Generalizer (Soon)

## Breakdown
### Core
Ingress of response traffic (to be eventually deferred to a stand-alone, network-handling module)\
This is accompanied by the resultant error handling on timed-out requests

The initial enumeration of the parsed result occurs here, till more sophistication is introduced.

### Menu Navigation
PyPokr is designed to be as interactive as possible. At least as much as a CLI can allow.\
A full graphical redesign shall occur after the rudimentary rendering has been ironed out. Candidates to include Qt5.

For HCI simplicity, the labels have relied on the following iconography: 

- ▲ for Up
- ▼ for Down

The currently selected option is highlighted with a ◄ icon

#### Linux platforms
```bash
^[[B
```
Navigation may present the following characters on your shell.\
This means there is a delay on refreshing after a key press has been logged 

### Generalizer
Since the program will be designed to consume responses from as many APIs as possible, abstraction over the content is handled here