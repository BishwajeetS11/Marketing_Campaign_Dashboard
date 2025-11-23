interface FilterDropdownProps {
  selectedStatus: string;
  onStatusChange: (status: string) => void;
}

export default function FilterDropdown({
  selectedStatus,
  onStatusChange,
}: FilterDropdownProps) {
  const statusOptions = ["All", "Active", "Paused"];

  return (
    <div className="flex items-center gap-2">
      <label
        htmlFor="status-filter"
        className="text-sm font-medium text-gray-700"
      >
        Filter by Status:
      </label>
      <select
        id="status-filter"
        value={selectedStatus}
        onChange={(e) => onStatusChange(e.target.value)}
        className="block w-40 px-3 py-2 text-sm border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white"
      >
        {statusOptions.map((status) => (
          <option key={status} value={status}>
            {status}
          </option>
        ))}
      </select>
    </div>
  );
}