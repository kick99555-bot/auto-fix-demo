def main():
    """Main function with error handling."""
    try:
        result = process_data()
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    return 0

def process_data():
    """Process data and return result."""
    return "Hello World"

if __name__ == "__main__":
    exit(main())
