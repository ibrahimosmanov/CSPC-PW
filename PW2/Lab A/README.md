## PW2 Lab A: Motion from Tracking Data

- **Mean Acceleration:** Measured mean acceleration is approximately $-9.81 \, m/s^2$, confirming that the object is in free fall.
- **Why Acceleration is Noisy:** Differentiation compares nearby measurements, which magnifies any small instrument noise present in the position data. Because acceleration requires two successive derivatives, the noise is amplified significantly, causing wild swings in the acceleration values while the position curve looks smooth.
- **Integration Results:** Integrating the noisy acceleration back to velocity and position using `cumulative_trapezoid` acts as a cumulative sum, which suppresses the random noise. The recovered position closely matches the original position, with a maximum difference of less than 1 metre.
