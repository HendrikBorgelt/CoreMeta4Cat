# Simulation

**Description:** The data class 'Simulation' describes the minimum information which should be reported 
with research data for conducting simulations in the field of catalysis.

---

## Main Class

<details>
<summary>### Simulation</summary>

**Description:** The data class 'Simulation' describes the minimum information which should be reported 
with research data for conducting simulations in the field of catalysis.

**URI:** `catcore:Simulation`

#### Slots (4)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>Simulation_software_package</strong></summary>

**Description:** Software or package used for simulation

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:software_package`

</details>

<details>
<summary><strong>Simulation_simulation_method</strong></summary>

**Description:** Simulation method used

**Range:** SimulationMethod

**Multivalued:** Yes

**URI:** `catcore:simulation_method`

**Range Class Details:**

<details>
<summary>##### SimulationMethod</summary>

**Abstract Class**

**Description:** Simulation method used

**URI:** `catcore:SimulationMethod`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

**Subclasses of SimulationMethod:**

<details>
<summary>###### DFT</summary>

**Description:** Density functional theory

**URI:** `catcore:DFT`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>exchange_correlation_functional</strong></summary>

**Description:** Exchange-correlation functional used (e.g., PBE, B3LYP)

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:exchange_correlation_functional`

</details>

<details>
<summary><strong>energy_cutoff</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:energy_cutoff`

**Unit:** eV

</details>

<details>
<summary><strong>convergence_criteria</strong></summary>

**Description:** Convergence criteria (e.g., energy, force)

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:convergence_criteria`

</details>

<details>
<summary><strong>dft_u_parameters</strong></summary>

**Description:** DFT+U parameters used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:dft_u_parameters`

</details>

<details>
<summary><strong>spin_polarization</strong></summary>

**Description:** Spin polarization setting

**Range:** boolean

**Multivalued:** Yes

**URI:** `catcore:spin_polarization`

</details>

<details>
<summary><strong>total_energy_per_atom</strong></summary>

**Description:** Total energy per atom

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:total_energy_per_atom`

**Unit:** eV

</details>

</details>

<details>
<summary>###### MolecularDynamics</summary>

**Description:** Molecular dynamics

**URI:** `NCIT:C18097`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>force_field</strong></summary>

**Description:** Force field used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:force_field`

</details>

<details>
<summary><strong>simulation_timestep</strong></summary>

**Description:** Time step for simulation

**Range:** float

**Multivalued:** Yes

**URI:** `APOLLO_SV:00000012`

**Unit:** fs

</details>

<details>
<summary><strong>simulation_time</strong></summary>

**Description:** Total simulation time

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:simulation_time`

**Unit:** ps

</details>

<details>
<summary><strong>ensemble_type</strong></summary>

**Description:** Ensemble type (e.g., NVT, NPT)

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:ensemble_type`

</details>

<details>
<summary><strong>number_of_atoms</strong></summary>

**Description:** Number of atoms in simulation

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_atoms`

</details>

</details>

<details>
<summary>###### Microkinetics</summary>

**Description:** Microkinetics simulation

**URI:** `catcore:Microkinetics`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>rate_constants</strong></summary>

**Description:** Rate constants or Arrhenius parameters

**Range:** string

**Multivalued:** Yes

**URI:** `NCIT:C94967`

</details>

<details>
<summary><strong>solver_type</strong></summary>

**Description:** Type of solver used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:solver_type`

</details>

<details>
<summary><strong>temperature</strong></summary>

**Description:** Temperature

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001584`

**Unit:** Cel

</details>

<details>
<summary><strong>pressure</strong></summary>

**Description:** Pressure in simulation

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:pressure`

**Unit:** bar

</details>

<details>
<summary><strong>surface_coverage</strong></summary>

**Description:** Surface coverage of species

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:surface_coverage`

</details>

<details>
<summary><strong>activation_energy</strong></summary>

**Description:** Activation energy for each step

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:activation_energy`

**Unit:** eV

</details>

</details>

<details>
<summary>###### MonteCarlo</summary>

**Description:** Monte Carlo simulation

**URI:** `catcore:MonteCarlo`

#### Slots (8)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>interaction_potential</strong></summary>

**Description:** Interaction potential used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:interaction_potential`

</details>

<details>
<summary><strong>number_of_steps</strong></summary>

**Description:** Number of Monte Carlo steps

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:number_of_steps`

</details>

<details>
<summary><strong>temperature</strong></summary>

**Description:** Temperature

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001584`

**Unit:** Cel

</details>

<details>
<summary><strong>lattice_size_type</strong></summary>

**Description:** Lattice size and type

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:lattice_size_type`

</details>

<details>
<summary><strong>acceptance_criteria</strong></summary>

**Description:** Acceptance criteria for Monte Carlo moves

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:acceptance_criteria`

</details>

<details>
<summary><strong>equilibration_steps</strong></summary>

**Description:** Number of equilibration steps

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:equilibration_steps`

</details>

<details>
<summary><strong>sampling_interval</strong></summary>

**Description:** Sampling interval for data collection

**Range:** integer

**Multivalued:** Yes

**URI:** `catcore:sampling_interval`

</details>

</details>

</details>

<details>
<summary><strong>Simulation_calculated_property</strong></summary>

**Description:** Property calculated from simulation

**Range:** CalculatedProperty

**Multivalued:** Yes

**URI:** `catcore:calculated_property`

**Range Class Details:**

<details>
<summary>##### CalculatedProperty</summary>

**Abstract Class**

**Description:** Property calculated from simulation

**URI:** `catcore:CalculatedProperty`

#### Slots (1)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

</details>

**Subclasses of CalculatedProperty:**

<details>
<summary>###### ThermodynamicStability</summary>

**Description:** Thermodynamic stability property

**URI:** `catcore:ThermodynamicStability`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>formation_energy</strong></summary>

**Description:** Formation energy per atom

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:formation_energy`

**Unit:** eV

</details>

<details>
<summary><strong>reference_energies</strong></summary>

**Description:** Reference elemental energies

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:reference_energies`

</details>

<details>
<summary><strong>energy_above_hull</strong></summary>

**Description:** Energy above convex hull

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:energy_above_hull`

**Unit:** eV

</details>

<details>
<summary><strong>phase_diagram_type</strong></summary>

**Description:** Phase diagram type (e.g., binary, ternary)

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:phase_diagram_type`

</details>

<details>
<summary><strong>competing_phases</strong></summary>

**Description:** Competing phase list

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:competing_phases`

</details>

</details>

<details>
<summary>###### Piezoelectricity</summary>

**Description:** Piezoelectricity property

**URI:** `catcore:Piezoelectricity`

#### Slots (5)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>piezoelectric_tensor</strong></summary>

**Description:** Piezoelectric tensor components

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:piezoelectric_tensor`

</details>

<details>
<summary><strong>crystal_symmetry</strong></summary>

**Description:** Crystal symmetry

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:crystal_symmetry`

</details>

<details>
<summary><strong>strain_applied</strong></summary>

**Description:** Strain applied

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:strain_applied`

</details>

<details>
<summary><strong>ionic_electronic_contributions</strong></summary>

**Description:** Ionic and electronic contributions

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:ionic_electronic_contributions`

</details>

</details>

<details>
<summary>###### ElasticConstants</summary>

**Description:** Elastic constants property

**URI:** `catcore:ElasticConstants`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>elastic_tensor</strong></summary>

**Description:** Elastic tensor components

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:elastic_tensor`

</details>

<details>
<summary><strong>bulk_modulus</strong></summary>

**Description:** Bulk modulus

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:bulk_modulus`

**Unit:** GPa

</details>

<details>
<summary><strong>shear_modulus</strong></summary>

**Description:** Shear modulus

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:shear_modulus`

**Unit:** GPa

</details>

<details>
<summary><strong>poisson_ratio</strong></summary>

**Description:** Poisson's ratio

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:poisson_ratio`

</details>

<details>
<summary><strong>young_modulus</strong></summary>

**Description:** Young's modulus

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:young_modulus`

**Unit:** GPa

</details>

</details>

<details>
<summary>###### Surfaces</summary>

**Description:** Surface property

**URI:** `catcore:Surfaces`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>surface_energy</strong></summary>

**Description:** Surface energy

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:surface_energy`

**Unit:** J/m2

</details>

<details>
<summary><strong>miller_indices</strong></summary>

**Description:** Miller indices of surface

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:miller_indices`

</details>

<details>
<summary><strong>slab_thickness</strong></summary>

**Description:** Slab thickness

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:slab_thickness`

**Unit:** angstrom

</details>

<details>
<summary><strong>vacuum_spacing</strong></summary>

**Description:** Vacuum spacing

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:vacuum_spacing`

**Unit:** angstrom

</details>

<details>
<summary><strong>surface_termination_method</strong></summary>

**Description:** Surface termination method

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:surface_termination_method`

</details>

</details>

<details>
<summary>###### DielectricTensors</summary>

**Description:** Dielectric tensors property

**URI:** `catcore:DielectricTensors`

#### Slots (6)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_composition</strong></summary>

**Description:** Material composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:material_composition`

</details>

<details>
<summary><strong>crystal_structure</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Multivalued:** Yes

**URI:** `SIO:001100`

</details>

<details>
<summary><strong>energy_cutoff</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:energy_cutoff`

**Unit:** eV

</details>

<details>
<summary><strong>convergence_criteria</strong></summary>

**Description:** Convergence criteria (e.g., energy, force)

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:convergence_criteria`

</details>

<details>
<summary><strong>k_point_mesh</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:k_point_mesh`

</details>

</details>

<details>
<summary>###### PhononDispersion</summary>

**Description:** Phonon dispersion property

**URI:** `catcore:PhononDispersion`

#### Slots (7)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_composition</strong></summary>

**Description:** Material composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:material_composition`

</details>

<details>
<summary><strong>crystal_structure</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Multivalued:** Yes

**URI:** `SIO:001100`

</details>

<details>
<summary><strong>force_constant_method</strong></summary>

**Description:** Force constant calculation method

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:force_constant_method`

</details>

<details>
<summary><strong>kq_point_mesh</strong></summary>

**Description:** k/q-point mesh for phonons

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:kq_point_mesh`

</details>

<details>
<summary><strong>smearing_parameter</strong></summary>

**Description:** Smearing/broadening parameter

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:smearing_parameter`

**Unit:** eV

</details>

<details>
<summary><strong>imaginary_modes</strong></summary>

**Description:** Imaginary modes present

**Range:** boolean

**Multivalued:** Yes

**URI:** `catcore:imaginary_modes`

</details>

</details>

<details>
<summary>###### EquationsOfState</summary>

**Description:** Equations of state property

**URI:** `catcore:EquationsOfState`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_composition</strong></summary>

**Description:** Material composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:material_composition`

</details>

<details>
<summary><strong>crystal_structure</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Multivalued:** Yes

**URI:** `SIO:001100`

</details>

<details>
<summary><strong>fit_method</strong></summary>

**Description:** Fit method (e.g., Birch-Murnaghan, Vinet)

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:fit_method`

</details>

<details>
<summary><strong>energy_cutoff</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:energy_cutoff`

**Unit:** eV

</details>

<details>
<summary><strong>k_point_mesh</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:k_point_mesh`

</details>

<details>
<summary><strong>bulk_modulus</strong></summary>

**Description:** Bulk modulus

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:bulk_modulus`

**Unit:** GPa

</details>

<details>
<summary><strong>pressure_derivative</strong></summary>

**Description:** Pressure derivative of bulk modulus

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:pressure_derivative`

</details>

<details>
<summary><strong>fit_residuals</strong></summary>

**Description:** Residuals of fit

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:fit_residuals`

</details>

</details>

<details>
<summary>###### AqueousStability</summary>

**Description:** Aqueous stability property

**URI:** `catcore:AqueousStability`

#### Slots (8)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_composition</strong></summary>

**Description:** Material composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:material_composition`

</details>

<details>
<summary><strong>crystal_structure</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Multivalued:** Yes

**URI:** `SIO:001100`

</details>

<details>
<summary><strong>ph_range</strong></summary>

**Description:** pH range considered

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:ph_range`

</details>

<details>
<summary><strong>potential_range</strong></summary>

**Description:** Potential range considered

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:potential_range`

</details>

<details>
<summary><strong>solvation_model</strong></summary>

**Description:** Solvation model used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:solvation_model`

</details>

<details>
<summary><strong>ionic_strength</strong></summary>

**Description:** Ionic strength of solution

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:ionic_strength`

**Unit:** mol/L

</details>

<details>
<summary><strong>temperature</strong></summary>

**Description:** Temperature

**Range:** float

**Multivalued:** Yes

**URI:** `AFR:0001584`

**Unit:** Cel

</details>

</details>

<details>
<summary>###### GrainBoundaries</summary>

**Description:** Grain boundaries property

**URI:** `catcore:GrainBoundaries`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_composition</strong></summary>

**Description:** Material composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:material_composition`

</details>

<details>
<summary><strong>grain_boundary_plane</strong></summary>

**Description:** Grain boundary plane

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:grain_boundary_plane`

</details>

<details>
<summary><strong>misorientation_angle</strong></summary>

**Description:** Misorientation angle

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:misorientation_angle`

**Unit:** deg

</details>

<details>
<summary><strong>grain_boundary_energy</strong></summary>

**Description:** Grain boundary energy

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:grain_boundary_energy`

**Unit:** J/m2

</details>

<details>
<summary><strong>simulation_cell_size</strong></summary>

**Description:** Simulation cell size

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:simulation_cell_size`

</details>

<details>
<summary><strong>gb_excess_volume</strong></summary>

**Description:** GB excess volume

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:gb_excess_volume`

</details>

<details>
<summary><strong>gb_structural_units</strong></summary>

**Description:** GB structural units description

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:gb_structural_units`

</details>

<details>
<summary><strong>charge_defect_segregation</strong></summary>

**Description:** Charge or defect segregation data

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:charge_defect_segregation`

</details>

</details>

<details>
<summary>###### ElectronicStructure</summary>

**Description:** Electronic structure property

**URI:** `catcore:ElectronicStructure`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_composition</strong></summary>

**Description:** Material composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:material_composition`

</details>

<details>
<summary><strong>crystal_structure</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Multivalued:** Yes

**URI:** `SIO:001100`

</details>

<details>
<summary><strong>k_point_mesh</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:k_point_mesh`

</details>

<details>
<summary><strong>energy_cutoff</strong></summary>

**Description:** Energy cutoff for plane wave basis

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:energy_cutoff`

**Unit:** eV

</details>

<details>
<summary><strong>smearing_method</strong></summary>

**Description:** Smearing method and width

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:smearing_method`

</details>

<details>
<summary><strong>spin_polarized</strong></summary>

**Description:** Spin-polarized calculation

**Range:** boolean

**Multivalued:** Yes

**URI:** `catcore:spin_polarized`

</details>

<details>
<summary><strong>band_path</strong></summary>

**Description:** Band path used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:band_path`

</details>

<details>
<summary><strong>fermi_energy</strong></summary>

**Description:** Fermi energy

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:fermi_energy`

**Unit:** eV

</details>

</details>

<details>
<summary>###### Ferroelectrics</summary>

**Description:** Ferroelectric property

**URI:** `catcore:Ferroelectrics`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_composition</strong></summary>

**Description:** Material composition

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:material_composition`

</details>

<details>
<summary><strong>crystal_structure</strong></summary>

**Description:** Crystal structure (space group, lattice parameters)

**Range:** string

**Multivalued:** Yes

**URI:** `SIO:001100`

</details>

<details>
<summary><strong>polarization_direction</strong></summary>

**Description:** Polarization direction

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:polarization_direction`

</details>

<details>
<summary><strong>spontaneous_polarization</strong></summary>

**Description:** Spontaneous polarization magnitude

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:spontaneous_polarization`

**Unit:** uC/cm2

</details>

<details>
<summary><strong>reference_structure</strong></summary>

**Description:** Reference paraelectric structure

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:reference_structure`

</details>

<details>
<summary><strong>switching_barrier</strong></summary>

**Description:** Switching barrier

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:switching_barrier`

**Unit:** eV

</details>

<details>
<summary><strong>coercive_field</strong></summary>

**Description:** Coercive field

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:coercive_field`

**Unit:** kV/cm

</details>

<details>
<summary><strong>temperature_dependence</strong></summary>

**Description:** Temperature dependence

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:temperature_dependence`

</details>

</details>

<details>
<summary>###### BandGap</summary>

**Description:** Band gap property

**URI:** `catcore:BandGap`

#### Slots (9)

<details>
<summary><strong>identifier</strong></summary>

**Description:** Unique identifier for the entity

**Range:** string

**Multivalued:** No

**URI:** `catcore:identifier`

</details>

<details>
<summary><strong>material_sample</strong></summary>

**Description:** Material sample

**Range:** string

**Multivalued:** Yes

**URI:** `voc4cat:0005056`

</details>

<details>
<summary><strong>structure_model</strong></summary>

**Description:** Structure or model used

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:structure_model`

</details>

<details>
<summary><strong>k_point_mesh</strong></summary>

**Description:** k-point mesh for sampling

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:k_point_mesh`

</details>

<details>
<summary><strong>smearing_broadening</strong></summary>

**Description:** Smearing or broadening parameter

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:smearing_broadening`

**Unit:** eV

</details>

<details>
<summary><strong>direct_indirect</strong></summary>

**Description:** Direct or indirect band gap

**Range:** string

**Multivalued:** Yes

**URI:** `catcore:direct_indirect`

</details>

<details>
<summary><strong>experimental_reference</strong></summary>

**Description:** Experimental reference value

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:experimental_reference`

**Unit:** eV

</details>

<details>
<summary><strong>gw_hybrid_correction</strong></summary>

**Description:** GW or hybrid correction used

**Range:** boolean

**Multivalued:** Yes

**URI:** `catcore:gw_hybrid_correction`

</details>

<details>
<summary><strong>excitonic_correction</strong></summary>

**Description:** Excitonic correction applied

**Range:** float

**Multivalued:** Yes

**URI:** `catcore:excitonic_correction`

**Unit:** eV

</details>

</details>

</details>

#### Slot Usage

- **software_package**: Required
- **simulation_method**: Required
- **calculated_property**: Required

</details>

