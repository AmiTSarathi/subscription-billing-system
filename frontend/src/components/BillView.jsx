
import { useEffect, useState } from 'react';

export default function BillView() {
  const [bill, setBill] = useState(null);

  useEffect(() => {
    fetch('http://localhost:8000/bill/user123')
      .then(res => res.json())
      .then(setBill);
  }, []);

  if (!bill) return <p>Loading bill...</p>;

  return (
    <div className="max-w-3xl mx-auto bg-white rounded-xl shadow p-6 space-y-4">
      <h1 className="text-xl font-bold">Subscription Bill</h1>
      <div className="text-sm text-gray-600">
        <p><strong>Bill ID:</strong> {bill.bill_id}</p>
        <p><strong>Name:</strong> {bill.user.name}</p>
        <p><strong>Date:</strong> {bill.bill_date}</p>
      </div>

      <table className="w-full mt-4 border text-sm">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 text-left">Subscription</th>
            <th>Base</th>
            <th>Discount</th>
            <th>Tax</th>
            <th>Final</th>
            <th>Currency</th>
          </tr>
        </thead>
        <tbody>
          {bill.items.map((item, idx) => (
            <tr key={idx} className="border-t">
              <td className="p-2">{item.description}</td>
              <td className="text-center">${item.base_amount}</td>
              <td className="text-center">-${item.discount_applied}</td>
              <td className="text-center">+${item.tax_applied}</td>
              <td className="text-center font-semibold">${item.final_amount}</td>
              <td className="text-center">{item.currency}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div className="text-right mt-4 text-lg font-bold">
        Total: ${bill.total_amount} {bill.currency}
      </div>
    </div>
  );
}
