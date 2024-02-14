import matplotlib.pyplot as plt


# Define the function to calculate the cost for a selected component based on n, m, and N
def calculate_component_cost(component, n, m, N):
    # Dictionary mapping component names to their cost formulas
    component_cost_formulas = {
        'тригер': 6,
        'регістр': 7 * n,
        'однорозрядний суматор': 18,
        'однорозрядний віднімач': 18,
        'однорозрядний суматор-віднімач': 20,
        'n-розрядний суматор': 20 * n,
        'n-розрядний віднімач': 21 * n,
        'n-розрядний суматор-віднімач': 23 * n,
        'm-вхідний n-розрядний суматор': (m - 1) * 20 * n,
        'm-вхідний, n- розрядний конвеєрний суматор': 27 * (m - 1) * n,
        'Пристрій множення': 18 * n ** 2,
        'Пристрій піднесення до квадрату': 9 * n ** 2,
        'пристрій ділення': 20 * n ** 2,
        'схема порівняння': 7 * n,
        'двійковий лічильник': 12 * n,
        'm-вхідний, n- розрядний комутатор': 3 * m * n,
        'm-вхідний n-розрядний ПЗП': 2 * m * n,
        'm- вхідний, n- розрядний ОЗП': 2 * m * 3 * n,
    }

    # Calculate the cost for the selected component
    if component in component_cost_formulas:
        cost_per_component = component_cost_formulas[component]
        total_cost = cost_per_component * N  # Total cost is cost per component times the number of components
        return total_cost
    else:
        raise ValueError(f"Component '{component}' not recognized.")


# Define a function to plot the dependency of equipment costs on N for selected components and n values
def plot_cost_dependency_on_N(components, n_values, N_range):
    plt.figure(figsize=(20, 10))

    # Plot for each 'n' value
    for i, n in enumerate(n_values, 1):
        plt.subplot(2, 2, i)

        # Plot cost dependency for each component
        for component in components:
            costs = [calculate_component_cost(component, n, m=1, N=N) for N in N_range]  # Assuming m=1 for simplicity
            plt.plot(N_range, costs, label=f"{component} (n={n})")

        plt.title(f"Cost Dependency on N for n={n}")
        plt.xlabel("Number of Components (N)")
        plt.ylabel("Total Equipment Cost")
        plt.grid(True)
        plt.legend()

    plt.tight_layout()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TASK 1
    selected_component = input("Enter the component name: ")
    n = int(input("Enter the number of functional nodes (bits) n: "))
    m = int(input("Enter the number of entries m: "))
    N = int(input("Enter the number of operands N: "))
    selected_comp_cost = calculate_component_cost(selected_component, n, m, N)
    print(selected_comp_cost)

    # TASK 2
    selected_components = ['регістр', 'n-розрядний суматор', 'm-вхідний n-розрядний суматор', 'm-вхідний, n- розрядний комутатор']
    n_values = [8, 16, 24, 32]  # Different 'n' values for the plots
    N_range = range(2, 22, 2)  # Range of 'N' values for which we want to show the cost dependency
    plot_cost_dependency_on_N(selected_components, n_values, N_range)

