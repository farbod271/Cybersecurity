# Logic Flaws and Testing

This document explains some common logic flaws and areas to pay attention to when testing applications. These flaws can often arise when messing around with the app to find unpredictable states.

## Key Points

- **Data Flow and Assumptions**: Mistakes can happen when one team assumes that another team's components have properly validated inputs. These assumptions can lead to logic flaws.
  
- **Low-Level Logic Flaws**: A classic example is the integer overflow during purchases. It's a common flaw where variables exceed their expected range.
  
- **Overflow of Variables**: Most examples of logic flaws involve overflowing variables. Be cautious when handling large values and variable limits.

- **Choosing Long Names**: Test how the app handles long names, as some systems may cut them off unexpectedly.

- **Session Handling**: Pay close attention to session changes and intermediary sessions that have privileges but are overwritten by requests.
