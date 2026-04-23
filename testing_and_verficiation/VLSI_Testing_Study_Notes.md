# VLSI Testing and Verification - Study Notes

## CO1: Fundamentals, Fault Modeling, and Simulation

---

### 1. Basics of Testing in VLSI Systems

VLSI testing encompasses all test methods and structures embedded in a system-on-chip (SOC) to ensure the quality of manufactured devices during manufacturing test. The purpose of VLSI testing is to verify functionality (could also include performance and reliability of ICs) and identify and correct any defects or faults. The testing process plays a crucial role in ensuring the robustness and safety of electronic devices. Without proper testing, ICs could malfunction, leading to system failures, safety hazards, and economic losses.

**Types of Tests:**

- **Characterization Testing (Design Debug):** Performed on a new design before it is sent to production. It verifies whether the design is correct and the device will meet all specifications. Comprehensive AC and DC measurements are made, and internal chip nodes may be probed.
- **Production Testing:** Less intensive test performed on every chip. The main driver is cost—test time must be minimized. Tests must have high coverage of modeled faults.
- **Parametric Tests:** DC parametric tests include shorts test, opens test, leakage test, etc. AC parametric tests include delay test, setup and hold test, etc.
- **Functional Tests:** Test every transistor and wire, designed to cover a high percentage of modeled faults.

---

### 2. Importance of Testing

As technology feature size of devices and interconnects shrink at the rate predicted by Moore's law, gate density and design complexity on a single integrated chip (IC) keep increasing. The close-to-nanoscale fabrication process introduces more manufacturing errors. New failure mechanisms that are not covered by current fault models are observed in designs fabricated in new technologies and new materials.

**Key Reasons for Testing:**

1. **Quality Assurance:** Ensures manufactured devices meet specifications
2. **Defect Detection:** Identifies manufacturing defects that could cause field failures
3. **Yield Improvement:** Helps identify process issues to improve manufacturing yield
4. **Reliability:** Ensures product quality and reliability over operational lifetime
5. **Cost Reduction:** Early detection of defects reduces the cost of rework and recalls

---

### 3. Test Challenges in IC Testing

The trend of testing costs for ICs with shrinking technology sizes is on the rise. As technology nodes shrink, the reduction in transistor and interconnect size leads to increased susceptibility to various types of defects and faults.

**Major Challenges:**

- **Increasing Complexity:** Billions of transistors in modern chips make comprehensive testing difficult
- **Multiple Clock Domains:** Complex timing relationships make at-speed testing challenging
- **Power Domains:** Multiple power domains with power gating require careful test planning
- **Embedded Memories:** Dense memory arrays are difficult to test without BIST
- **Speed Testing:** Test at speed of application or speed guaranteed by the supplier
- **Fault Coverage:** Achieving high fault coverage for complex designs is challenging
- **Test Data Volume:** Large test data sets require significant storage and transfer time
- **Test Cost:** Test equipment (ATE) is expensive, and test time directly impacts cost

---

### 4. Defects, Errors, and Faults

**Defect:** An unintended difference between the implemented hardware and its intended design. Defects occur either during manufacture or during the use of devices. They can be permanent (incorrect manufacturing, shorts, bridges, missing transistors) or non-permanent (parametric defects, functional design errors).

**Error:** A wrong output signal produced by a defective system. An error is caused by a fault or a design error.

**Fault:** A representation of a defect at the abstracted function level. A fault is a logic level abstraction of a physical defect used to describe the change in the logic function of a device caused by the defect. Fault abstractions reduce the number of conditions that must be considered in deriving tests.

**Fault Model:** A collection of faults, all of which are based on the same set of assumptions concerning the nature of defects.

---

### 5. Functional vs Structural Testing

**Functional Testing:**

- Tests the I/O function of the circuit
- Too long test time for real circuits with hundreds of inputs
- Useful for verification of design (before manufacturing)
- Does not targeting specific manufacturing defects

**Structural Testing:**

- Uses fault models allowing development of test algorithms
- Reduces test complexity
- Technology-independent fault models and tests
- Focuses on detecting modeled faults rather than verifying function
- Enables automatic test pattern generation (ATPG)

**Checkpoint Theorem:** A test set that detects all single (multiple) stuck-at faults on all checkpoints of a combinational circuit also detects all single (multiple) stuck-at faults in that circuit. Primary inputs and fanout branches of a combinational circuit are called checkpoints.

---

### 6. Fault Modeling Stages

Fault models can be formulated at various levels of design abstraction:

1. **Behavioral Level:** Faults may not have any obvious correlation to defects
2. **RTL and Logic Level:** Stuck-at faults most popular, followed by bridging and delay fault models
3. **Transistor (Switch) Level:** Technology-dependent faults
4. **Design Level Independent Fault Model:** IDDQ—can represent defects not represented by any other model

**Common Fault Models:**

- **Stuck-at Faults:** Line stuck at 0 or 1
- **Bridging Faults:** Unintended connection between two lines
- **Stuck-open Faults:** Transistor permanently open
- **Stuck-short Faults:** Transistor permanently shorted
- **Delay Faults:** Timing violations (transition, gate-delay, line-delay, path-delay)
- **Coupling Faults:** Fault in one cell affects another cell
- **Address Decoder Faults:** Issues in memory address decoding

---

### 7. Stuck-at Faults

The single stuck-at fault model is the most widely used fault model in digital logic testing. It offers the best advantage of tools and experience. Many other faults (bridging, stuck-open, and multiple stuck-at) are largely covered by stuck-at fault tests.

**Types of Stuck-at Faults:**

- **Single Stuck-at Fault:** One line in the circuit is stuck at 0 or 1
- **Multiple Stuck-at Fault:** Any set of lines is stuck at some combination of (0,1) values

**Classes of Single Stuck-at Faults:**

- **Safely detectable:** Test exists that detects the fault
- **Potentially detectable:** Fault prevents initialization of the circuit
- **Redundant:** No test can detect the fault
- **Equivalent:** Two faults f1 and f2 are equivalent if all tests that detect f1 also detect f2 and vice versa

**Fault Equivalence:** If faults f1 and f2 are equivalent, only one needs to be considered. This reduces the number of faults to be analyzed.

---

### 8. Logic Simulation (Concept + Role in Verification)

Logic simulation is the process of modeling the behavior of a digital circuit to verify its correctness. It is an essential part of the design verification process.

**Role in Verification:**

- **Design Verification:** Ensures the design meets specifications before manufacturing
- **Debugging:** Helps identify design errors early in the design cycle
- **Test Development:** Test vectors can be simulated before actual testing
- **Fault Modeling Verification:** Validates that fault models accurately represent potential defects

**Types of Logic Simulation:**

- **Behavioral Simulation:** Models circuit at functional level
- **RTL Simulation:** Models circuit at register transfer level
- **Gate-level Simulation:** Models circuit at logic gate level
- **Switch-level Simulation:** Models circuit at transistor level

**Zero-delay Assumption:** All gates have the same delay (zero or unit), and signals assume only binary, 0 or 1 values.

---

### 9. Circuit Modeling for Evaluation

The circuit model for evaluation includes modeling the expected behavior and comparing it with actual behavior. ATE (Automatic Test Equipment) is an instrument built to apply test patterns to a device under test (DUT), analyze the responses from the DUT, and mark the DUT as faulty or fault-free.

**Key Aspects:**

- **Fault-free Circuit Model:** C(0) — the original circuit without faults
- **Faulty Circuit Model:** C(f) — the circuit with fault f injected
- **Test Vector Application:** Applying inputs to detect specific faults
- **Output Comparison:** Comparing expected vs. actual outputs

**Circuit Model Assumptions for Simulation:**

- Circuit consists of only logic gates
- Stuck-at faults are modeled
- All gates have the same delay (zero or unit)
- Signals assume only binary, 0 or 1 values

---

### 10. Fault Simulation Algorithms

Fault simulation is the process of simulating the response of a logic circuit to input patterns in the presence of all possible single faults. It is an essential part of test generation for VLSI circuits.

#### Serial Fault Simulation

- Simulate fault-free circuit once
- Then simulate one faulty circuit at a time
- Most effective when circuits C(fn) are almost identical
- If fault dropping is employed, simulation stops when all w-1 faults are detected

#### Parallel Fault Simulation

- Simulate all circuits (fault-free and faulty) simultaneously
- Uses bit-parallelism of logical operations in a computer
- For a 32-bit word, 1 fault-free and 31 faulty circuits can be simultaneously simulated
- Compiled-code or event-driven versions are possible

#### Deductive Fault Simulation

- Only the fault-free circuit, C(0), is simulated
- Faulty circuit values are deduced from the fault-free values
- Processes all faults in a single pass of true-value simulation (very fast!)
- Fault lists are generated for each signal using the fault lists on the inputs to the gate generating that signal
- A deductive procedure is performed on all lines in level-order from inputs to outputs

#### Concurrent Fault Simulation

- Simulates fault-free and faulty circuits concurrently
- Uses less memory than parallel fault simulation
- More efficient for large circuits with many faults

---

### 11. Statistical Fault Simulation Approaches

**Random Pattern Generation (RPG):**

- Fault simulation is essential to select useful patterns
- RPG saturates at 60-80% fault coverage
- D-algo needed to improve for hard-to-test faults

**Hybrid Approaches:**

- Use RPG first to achieve 60-80% coverage
- Then use deterministic ATPG (D-algorithm, PODEM, FAN) for remaining faults
- This approach is more efficient than using ATPG alone

**Statistical Fault Simulation:**

- Uses statistical methods to estimate fault coverage
- Reduces computational complexity for large circuits
- Provides approximate coverage estimates quickly

---

### 12. Complete Test Flow (Modeling, Simulation, Evaluation)

The complete test flow involves:

1. **Fault Modeling:** Define the fault model to be used (e.g., stuck-at, bridging, delay)
2. **Test Generation:** Generate test vectors using ATPG or functional vectors
3. **Fault Simulation:** Evaluate test vectors to measure fault coverage
4. **Evaluation:** Assess test quality using metrics like fault coverage, defect level, and test effectiveness

**Steps in Complete Test Flow:**

1. Select fault model based on technology and defect types
2. Generate test vectors using ATPG algorithms
3. Perform fault simulation to evaluate coverage
4. Identify undetected faults
5. Generate additional tests for undetected faults
6. Repeat until target coverage is achieved
7. Evaluate test cost vs. coverage tradeoff

**Test Quality Measures:**

- **Fault Coverage:** Percentage of modeled faults detected by test set
- **Defect Level:** Percentage of defective chips passing tests
- **Test Effectiveness:** Ability to detect real-world defects

---

## CO2: Test Generation and ATPG

---

### 11. Fundamentals of Test Generation (Combinational Circuits)

Test generation for combinational circuits involves finding input vectors that can detect specific faults. For a given fault, the test must:

1. **Activate the fault** (excite): Force the line with the fault to have the opposite value from the fault value
2. **Propagate the fault effect** to a primary output (sensitize): Create a path from the fault site to an observable output
3. **Justify the required values** (consistency): Ensure all required input values are consistent

**Key Concepts:**

- **Fault Cone:** The portion of a circuit whose signals are reachable by a forward trace of the circuit topology starting at the fault site
- **Controllability:** Ease of setting a node to 0 or 1
- **Observability:** Ease of observing the value at a node at a primary output

---

### 12. Test Generation Algorithms (Combinational)

**Path Sensitization Method:**

- Find a path from fault site to primary output
- Set all side inputs on the path to non-controlling values
- Justify the required value at fault site
- Simple but not systematic for computer implementation

**D-Calculus:**

- Uses 5-valued logic: 0, 1, X, D (1/0), D' (0/1)
- D represents the difference between good and faulty circuit
- D' is the complement of D

---

### 13. Redundant Faults in Combinational Circuits

**Redundant Fault:** A fault for which no test exists that can detect it. These faults do not affect the circuit function and can be safely ignored in test generation.

**Identification of Redundancy:**

- ATPG algorithm proves redundancy if it exhausts all possibilities without finding a test
- Redundant faults indicate unnecessary circuit logic
- Can be removed to improve area and performance

**Types of Redundancy:**

- **Structural Redundancy:** Duplicate logic that can be removed
- **Functional Redundancy:** Logic that doesn't affect output for any input

---

### 14. Combinational ATPG Algorithms

#### D-Algorithm (Roth, 1966)

The first complete test pattern algorithm designed to be programmable on a computer. Uses cubical algebra.

**Steps:**

1. Select a primitive D-cube of failure (PDCF) for fault activation
2. Propagate D to primary outputs using propagation D-cubes (D-drive)
3. Justify internal signals using singular covers (consistency check)

**Key Concepts:**

- **Primitive D-cube of failure (PDCF):** Defines the conditions for fault excitation
- **Propagation D-cube (PDC):** Defines how to propagate fault effect through a gate
- **Singular Cover:** Defines conditions for justifying signal values

#### PODEM (Goel, 1981)

Uses path propagation constraints to limit ATPG search space. Introduces backtracing.

**Key Features:**

- Uses objectives to guide search
- Considers only primary input assignments
- More efficient than D-algorithm for large circuits
- Backtrace: Converts objective to primary input assignments

#### FAN (Fujiwara, 1985)

Efficiently constrained the backtrace to speed up search and further limited the search space.

**Key Features:**

- Multiple backtracing
- Uses essential prime implicants
- More efficient than PODEM

**Comparison:**

| Algorithm | Year | Key Feature |
|-----------|------|------------|
| D-Algorithm | 1966 | First complete algorithm using cubical algebra |
| PODEM | 1981 | Path constraints, backtracing |
| FAN | 1985 | Efficient backtrace, essential prime implicants |

---

### 15. Test Generation Systems (Functioning)

**ATPG System Components:**

1. **Fault List Manager:** Manages list of faults to be targeted
2. **Implication Engine:** Computes implications of assignments
3. **Search Engine:** Searches for test vectors
4. **Compactor:** Reduces test set size after generation

**Test Generation Process:**

1. Initialize fault list
2. Select target fault
3. Run ATPG algorithm
4. If test found, record it and drop detected faults
5. If no test found, mark fault as redundant
6. Repeat until all faults processed

**Test Compaction:**

- **Static Compaction:** Compatible patterns are merged
- **Dynamic Compaction:** New patterns are added to cover additional faults

---

### 16. Sequential Circuit Test Generation Principles

Sequential circuit testing is more complex than combinational testing due to:

1. **State Dependency:** Circuit behavior depends on current state
2. **Memory Elements:** Internal flip-flops are not directly controllable/observable
3. **Initialization Requirement:** Circuit must be initialized to known state before testing

**Test Sequence Requirements:**

A test for a fault in a sequential circuit is a sequence of vectors that:

- Initializes the circuit to a known state
- Activates the fault
- Propagates the fault effect to a primary output

**Challenges:**

- Sequential depth: Number of time frames needed
- State initialization: Finding initialization sequence
- Long test sequences: Exponential complexity

---

### 17. Sequential ATPG Algorithms

#### Time-Frame Expansion (TFE) Method

The circuit is replicated multiple times to represent different time frames. Combinational ATPG can be used on the expanded circuit.

**Process:**

1. Replicate combinational logic block n times (n = number of time frames)
2. Place fault in each block
3. Generate test using combinational ATPG with 9-valued logic

**Nine-Valued Logic (Muth):** Extension of 5-valued D-calculus to handle sequential circuits with states {0, 1, X, D, D', F, F', G, G'}

#### Simulation-Based Approach

Uses fault simulation to evaluate randomly generated sequences. Less efficient but simpler to implement.

#### Scan-Based Testing

Scan design eliminates sequential complexity by converting flip-flops to scan chains. This allows direct control and observation of internal states.

---

### 18. BIST Concepts and Strategies

**Built-In Self-Test (BIST):** A design technique in which parts of the circuit are used to test the circuit itself. This reduces dependence on external test equipment.

**BIST Advantages:**

- At-speed testing possible
- Reduces test data volume
- Reduces test application time
- Lower test cost

**BIST Architectures:**

1. **Internal BIST:** Test logic inside the chip
2. **External BIST:** Test logic outside the chip (but still on-board)
3. **Hybrid BIST:** Combination of internal and external

**BIST Pattern Generation:**

- **Pseudo-random patterns:** Generated using LFSR (Linear Feedback Shift Register)
- **Deterministic patterns:** Pre-generated for specific faults

**On-chip Testing:**

- BIST can make effective use of test point insertion
- Control points can be added in troublesome regions, treated as PIs by BIST circuitry

---

### 19. Application of Combinational ATPG

Combinational ATPG is applied after scan design converts sequential circuits to combinational ones.

**Typical Flow:**

1. Insert scan chains
2. Run combinational ATPG on modified circuit
3. Achieve high fault coverage (typically >99%)
4. Apply test vectors through scan chains

**Test Modes:**

- **Normal Mode:** Circuit operates functionally
- **Shift Mode:** Data shifted through scan chains
- **Capture Mode:** Response captured in scan flip-flops

---

### 20. End-to-End Test Generation Flow

**Complete Test Generation Flow:**

1. **Design Analysis:** Analyze circuit for testability issues
2. **DFT Insertion:** Add scan chains, test points, BIST
3. **Test Generation:** Generate test vectors using ATPG
4. **Fault Simulation:** Evaluate fault coverage
5. **Test compaction:** Reduce test vector count
6. **Test Verification:** Verify tests on silicon

**Target Fault Coverage:**

- Typically 95-99% for production test
- Higher coverage for safety-critical applications
- Remaining faults may be redundant or untestable

---

## CO3: DFT and Memory Testing

---

### 21. Fundamentals of DFT

**Design for Testability (DFT):** Refers to those design techniques that enhance testability of a device, ease ability to generate vectors, reduce test time, and reduce cost involved during test.

**DFT Goals:**

- Improve controllability and observability
- Reduce test generation complexity
- Increase fault coverage
- Reduce test cost

**Two Categories:**

1. **Ad-hoc Methods:** Good design practices and guidelines
2. **Structured Methods:** Systematic approaches like scan, BIST, boundary scan

---

### 22. Ad-hoc DFT Techniques

**Ad-hoc DFT Guidelines:**

- Avoid combinational feedback loops
- All flip-flops must be initializable
- Avoid redundant and large fan-in gates
- Provide test control for signals not controllable
- Partition large circuits into smaller modules
- Consider ATE requirements while designing test logic

**Disadvantages of Ad-hoc Methods:**

- Experts and tools not always available
- Test generation is often manual with no guarantee of high fault coverage
- Design iterations may be necessary

**Key Ad-hoc Techniques:**

- **Partitioning:** Divide circuit into smaller testable modules
- **Test Points:** Add control points (CP) and observation points (OP)
- **Initialization:** Ensure sequential circuits can be initialized

---

### 23. Scan-Based Design Elements and Purpose

**Scan Design:** The most widely used structured DFT methodology. Converts sequential elements into a testable structure.

**Purpose:**

- Improve testability by improving controllability and observability of storage elements
- Convert sequential circuit testing to combinational testing
- Enable at-speed testing
- Achieve high fault coverage

**Scan Flip-Flop:** A flip-flop with a multiplexer at the input, allowing either normal data or scan data to be captured.

**Scan Chain:** Connect scan flip-flops in a shift register configuration for test data shift-in and shift-out.

---

### 24. Generic Scan Design Structure

**Scan Design Modes:**

1. **Normal Mode:** Circuit operates functionally (SE = 0)
2. **Shift Mode:** Data shifted through scan chain (SE = 1, capture disabled)
3. **Capture Mode:** Response captured in flip-flops (SE = 0, capture enabled)

**Scan Design Process:**

1. Convert all flip-flops to scan flip-flops
2. Connect scan flip-flops into scan chains
3. Add test access ports (TDI, TDO, SE, TCK)
4. Generate test vectors using ATPG

**Scan Architecture:**

- **Full Scan:** All flip-flops are in scan chains
- **Partial Scan:** Only some flip-flops are in scan chains
- **Multiple Scan Chains:** Parallel chains for reduced test time

---

### 25. Generic vs Classical Scan Design

**Muxed-D Scan (Classical):**

- Most common scan style
- 2:1 multiplexer before D input
- Scan Enable (SE) controls mode
- Simple, widely supported

**Level Sensitive Scan Design (LSSD):**

- Separate shift and capture clocks
- More robust for radiation hardening
- Better testability for async circuits

**Scan-Hold Flip-Flops (SHFF):**

- Hold latch added after scan flip-flop
- Decouples scan and functional modes
- Ideal for delay fault testing
- ~30% area overhead

**Random-Access Scan (RAS):**

- Individual flip-flops accessed via address
- Like RAM cells
- Reduced scan time but increased area

---

### 26. System-Level DFT Approaches

**Boundary Scan (IEEE 1149.1):**

- Most successful test standard
- Initially for board-level testing
- Now used for chip-level too
- Provides access to chip I/Os
- Allows testing of interconnects and板上组件

**Core-Based Testing:**

- Test embedded cores in SOC
- Test access mechanism (TAM)
- Wrapper design around cores
- IEEE P1500 standard

**Test Access Mechanisms:**

- **Scan-based TAM:** Using scan chains
- **Mux-based TAM:** Using multiplexers
- **Distributed TAM:** Distributed with wrapper

---

### 27. Self-Test Concepts (Application to Blocks)

**Built-In Self-Test (BIST):** Test logic is integrated into the chip to test itself.

**BIST for Logic:**

- LFSR for pseudo-random pattern generation
- MISR (Multiple Input Signature Register) for response compaction
- Self-test controller manages test execution

**BIST Process:**

1. Load LFSR with seed
2. Generate patterns
3. Apply to CUT
4. Capture response in MISR
5. Compare signature

**Logic BIST Advantages:**

- At-speed testing
- No test vector storage
- Low test cost

**Logic BIST Limitations:**

- Lower fault coverage than deterministic ATPG
- May miss hard-to-detect faults

---

### 28. Memory Fault Analysis Using Test Algorithms

**Memory Fault Models:**

- **Stuck-at Faults (SAF):** Cell stuck at 0 or 1
- **Transition Faults (TF):** Inability to transition from 0 to 1 or 1 to 0
- **Coupling Faults (CF):** Write operation on one cell affects another
  - Inversion Coupling (CFin): Inverts value in coupled cell
  - Idempotent Coupling (CFid): Forces coupled cell to 0 or 1
  - State Coupling (CFst): Coupled cell depends on state of coupling cell
- **Address Decoder Faults (AF):** No cell accessed, multiple cells accessed, or wrong cell accessed
- **Pattern Sensitive Faults (NPSF):** Content of a cell affected by pattern in neighboring cells

**Test Algorithms:**

- **Zero-One Algorithm:** Simplest, detects stuck-at faults
- **Checkerboard Algorithm:** Alternating pattern for detecting coupling faults
- **March Algorithms:** Most effective for memory testing

---

### 29. Embedded RAM Test Generation

**March Algorithm:** A widely used algorithm that tests SRAM by marching through memory addresses.

**March Notation:**

- ↑: Address increasing order
- ↓: Address decreasing order
- ↕: Either direction
- w0/w1: Write 0/1
- r0/r1: Read 0/1 (expecting 0/1)

**Common March Algorithms:**

| Algorithm | Complexity | Faults Detected |
|-----------|------------|-----------------|
| March A | 7N | SAF, TF |
| March B | 10N | SAF, TF, CF |
| March C- | 10N | SAF, TF, CF, AF |
| March X | 6N | SAF, TF |
| March LR | 14N | SAF, TF, CF, AF, CFid |

**March C-:** {↕(w0); ↑(r0, w1); ↑(r1, w0); ↓(r0, w1); ↓(r1, w0); ↕(r0)}

---

### 30. DFT + BIST for Memory Optimization

**Memory BIST (MBIST):** Integrated BIST for memory testing.

**MBIST Architecture:**

- BIST controller
- March test algorithm engine
- Address generator
- Data generator
- Comparator

**MBIST Advantages:**

- At-speed testing
- No external test patterns needed
- Fast fault detection and location
- Can be embedded in SOC

**Test Algorithms Used with MBIST:**

- March C-: High fault coverage, low complexity
- March LR: Higher coverage for complex faults
- March SS: Detects pattern sensitive faults

**Memory Built-In Self-Repair (MBISR):**

- Uses spare rows/columns
- Replaces faulty cells with spares
- Improves yield

**Optimization Techniques:**

- **Parallel Testing:** Multiple memories tested simultaneously
- **Shared BIST:** One BIST controller tests multiple memories
- **Reduced Complexity:** Lower number of March operations while maintaining coverage

---

## Key Formulas and Relationships

**Defect Level (DL):** DL = 1 - Y^(1-FC)

- Y: Yield
- FC: Fault Coverage

As fault coverage increases, defect level decreases exponentially.

**Test Complexity (March):** Expressed as N times complexity, where N = number of memory locations

**Fault Coverage Formula:**

```
Fault Coverage = (Faults Detected / Total Faults) × 100%
```

---

## Quick Reference Summary

| Topic | Key Points |
|-------|-----------|
| Fault Models | Stuck-at, Bridging, Delay, Coupling |
| ATPG Algorithms | D-Algorithm, PODEM, FAN |
| DFT Techniques | Scan, BIST, Boundary Scan |
| Memory Testing | March Algorithms, Checkerboard |
| Fault Simulation | Serial, Parallel, Deductive |

---

## Important Definitions

- **Checkpoint:** Primary inputs and fanout branches in combinational circuits
- **Fault Collapsing:** Reducing equivalent faults
- **D-Frontier:** Gates with D at inputs and X at output
- **Controllability:** Ease of setting node to 0/1
- **Observability:** Ease of observing node at PO
- **Scan Chain:** Shift register of scan flip-flops
- **March Element:** Single operation (read/write) applied to all addresses

---

*Study notes compiled for exam preparation. Refer to Bushnell & Agrawal "Essentials of Electronic Testing for Digital, Memory and Mixed-Signal VLSI Circuits" for detailed coverage.*