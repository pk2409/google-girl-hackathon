export function Button({ children, className = "", ...props }) {
  return (
    <button
      className={`px-4 py-2 border border-black bg-blue-500 text-black-500 rounded ${className}`}
      {...props}
    >
      {children}
    </button>
  );
}
