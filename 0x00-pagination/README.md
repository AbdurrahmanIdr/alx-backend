# Pagination Project

This repository contains the implementation of a pagination system for a dataset of popular baby names. The project includes various tasks to implement and test different pagination techniques.

## Project Structure

The project is structured as follows:

- **0-simple_helper_function.py**: Contains the `index_range` function to calculate pagination indexes.
- **1-simple_pagination.py**: Implements the `Server` class with a `get_page` method for simple pagination.
- **2-hypermedia_pagination.py**: Extends the `Server` class to include a `get_hyper` method for hypermedia pagination.
- **3-hypermedia_del_pagination.py**: Further extends the `Server` class with a `get_hyper_index` method for deletion-resilient pagination.
- **Popular_Baby_Names.csv**: The dataset used for the project.
- **0-main.py**, **1-main.py**, **2-main.py**, **3-main.py**: Main files to test each task.

## Getting Started

### Prerequisites

- Python 3.7
- Ubuntu 18.04 LTS

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/AbdurrahmanIdr/alx-backend.git
   ```
2. Navigate to the project directory:
   ```sh
   cd alx-backend/0x00-pagination
   ```
3. Ensure the dataset `Popular_Baby_Names.csv` is in the project directory.

### Usage

1. Run the main files to test each task:
   ```sh
   ./0-main.py
   ./1-main.py
   ./2-main.py
   ./3-main.py
   ```

## Tasks

### Task 0: Simple Helper Function

- Implemented the `index_range` function to return start and end indexes for pagination.

### Task 1: Simple Pagination

- Added the `Server` class with a `get_page` method to paginate the dataset.
- Validates parameters to ensure they are positive integers.

### Task 2: Hypermedia Pagination

- Implemented the `get_hyper` method to provide hypermedia pagination with metadata.

### Task 3: Deletion-Resilient Hypermedia Pagination

- Added the `get_hyper_index` method to ensure pagination is resilient to deletions in the dataset.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [REST API Design: Pagination](https://restfulapi.net/pagination/)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)